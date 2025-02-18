package mdb

/*
#include "zd_cgo.h"
*/
import "C"
import "sync"
import "core/mysql"
import "fmt"
import "runtime"
import "time"
import "core/syncutil"
import "os"
import "unsafe"

//import (
//	"core/debug"
//	corelog "core/log"
//)

const (
	FILE_COMMIT_CHAN_BUF_MAX  = 50000 * 2
	MYSQL_COMMIT_CHAN_BUF_MAX = 50000 * 2
	TLOG_COMMIT_CHAN_BUF_MAX  = 50000 * 2
	XDLOG_COMMIT_CHAN_BUF_MAX = 50000 * 2
)

var (
	g_Database       *Database // 用于全局事务
	g_MysqlCommitter *mysqlCommitter
	g_FileCommitter  *fileCommitter
	g_LockManager    *lockManager
	g_GlobalLock     syncutil.RWMutex // 用于全局事务和玩家事务互斥
	g_PlayerTables   map[int64]*C.PlayerTables
)

func init() {
	C.Init()

	g_LockManager = newLockManager()
	g_GlobalLock = syncutil.NewRWMutex(new(sync.RWMutex))
	g_PlayerTables = make(map[int64]*C.PlayerTables)
}

func GetPlayerTables(pid int64) *C.PlayerTables {
	return g_PlayerTables[pid]
}

func CheckPlayer(pid int64) bool {
	_, ok := g_PlayerTables[pid]
	return ok
}

func SetPlayerTables(tables *C.PlayerTables) {
	if _, exists := g_PlayerTables[int64(tables.Pid)]; exists {
		panic("duplicate set player tables")
	}
	g_PlayerTables[int64(tables.Pid)] = tables
}

// 启动内存数据库，映射mysqlInfo对应的数据库
func Start(globalServer bool, serverId int, mysqlInfo map[string]interface{}, dbFileDir string, tlogDir string, xdlogDir string, enablexdlog, enabletlog bool) {

	g_MysqlCommitter = newMySqlCommitter(mysqlInfo)
	g_FileCommitter = newFileCommitter(g_MysqlCommitter, fmt.Sprintf("%s/srv-%d/", dbFileDir, serverId), fmt.Sprintf("%s/srv-%d/", tlogDir, serverId), fmt.Sprintf("%s/srv-%d/", xdlogDir, serverId), enablexdlog, enabletlog)

	g_Database = NewDatabase() // 必须要在g_LockManager，g_MysqlCommitter之后初始化

	db, err1 := mysql.Connect(mysqlInfo)
	if err1 != nil {
		panic(err1)
	}
	defer db.Close()

	initRowIdsWithServerId(int64(serverId) << 32)

	// 初始化所有玩家的数据库切片
	newPlayerTables(db)

	wg := new(sync.WaitGroup)
	wgn := runtime.GOMAXPROCS(-1)

	// 加载互动服数据
	if globalServer {

		initGlobalTables(db)

		goLoad(mysqlInfo, wgn, wg, func(newDB *mysql.Connection, procId int) {
			initPlayerGlobalTables(newDB, serverId, wgn, procId)
		})

	} else {
		// 加载游戏服数据

		goLoad(mysqlInfo, wgn, wg, func(newDB *mysql.Connection, procId int) {
			initPlayerTables(newDB, serverId, wgn, procId)
		})
	}

	wg.Wait()
	fmt.Println("mdb.load success.")
}

func goLoad(mysqlInfo map[string]interface{}, wgn int, wg *sync.WaitGroup, callback func(*mysql.Connection, int)) {
	for i := 0; i < wgn; i++ {
		wg.Add(1)
		go func(procId int) {
			var t1 = time.Now()
			db, err1 := mysql.Connect(mysqlInfo)
			if err1 != nil {
				panic(err1)
			}
			defer db.Close()
			callback(db, procId)
			wg.Done()
			fmt.Printf("mdb.load (%d) cost time: %v\n", procId, time.Now().Sub(t1))
		}(i)
	}
}

func Stop(enablexdlog, enabletlog bool) {
	g_FileCommitter.Stop(enablexdlog, enabletlog)
}

func Transaction(transId uint32, work func()) {
	g_GlobalLock.Lock()
	defer g_GlobalLock.Unlock()

	g_Database.Transaction(transId, work)
}

// 互动服挂着玩家数据
func GlobalMount(db *Database, playerId int64) {
	db.mountTables(playerId)
}

// GlobalExecute要配合Transaction使用
func GlobalExecute(cb func(*Database)) {
	cb(g_Database)
}

// 互动服务器初始化特定玩家数据库切片
func NewPlayerTablesWithDatabase(db *Database, playerId, cId int64) {
	if GetPlayerTables(playerId) != nil {
		panic("player tables exists")
	}

	playerDB := C.NewPlayerTables()
	playerDB.Pid = C.int64_t(playerId)
	SetPlayerTables(playerDB)

	db.playerId = playerId
	db.cId = int32(cId)
	db.tables = playerDB
}

func ProfileFileCommitToLog(enablexdlog, enabletlog bool) {
	g_FileCommitter.ProfilePrintToLog(enablexdlog, enabletlog)
}

func ProfileFileCommitToFile(fp *os.File, enablexdlog, enabletlog bool) {
	g_FileCommitter.ProfileWriteToFile(fp, enablexdlog, enabletlog)
}

func PrepareOnlineInfoToOnlineTable(db *mysql.Connection, tableName string) *mysql.Stmt {
	return prepare(db, fmt.Sprintf("INSERT INTO `%s` (`gameappid`, `timekey`, `gsid`, `onlinecntios`, `onlinecntandroid`, `cid`)VALUES(?,?,?,?,?,?)", tableName))
}

func PreparePresentRuleInfoToPresentRuleTable(db *mysql.Connection, tableName string) *mysql.Stmt {
	return prepare(db, fmt.Sprintf("update `%s` set `rule`= ?,`begin_time`= ?,`end_time`=?", tableName))
}

func DoInsertOnline(stmt *mysql.Stmt, gameappid string, timekey, gsid, onlinecntios, onlinecntandroid, cid int64) error {
	stmt.CleanBind()
	stmt.BindVarchar(unsafe.Pointer(C.CString(string(gameappid))), int(C.int(len(gameappid))))
	stmt.BindBigInt(unsafe.Pointer(&timekey))
	stmt.BindBigInt(unsafe.Pointer(&gsid))
	stmt.BindBigInt(unsafe.Pointer(&onlinecntios))
	stmt.BindBigInt(unsafe.Pointer(&onlinecntandroid))
	stmt.BindBigInt(unsafe.Pointer(&cid))
	return stmt.Execute()
}

func DoUpdateRule(stmt *mysql.Stmt, rule string, begintime, endtime int64) error {
	stmt.CleanBind()
	stmt.BindVarchar(unsafe.Pointer(C.CString(string(rule))), int(C.int(len(rule))))
	stmt.BindBigInt(unsafe.Pointer(&begintime))
	stmt.BindBigInt(unsafe.Pointer(&endtime))
	return stmt.Execute()
}
