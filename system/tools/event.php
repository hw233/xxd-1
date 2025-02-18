<?php
/*
 * 操作步骤
 * 假定创建的活动标识为xxx 
 * 1.在pages/quest_activity_center_extend.php中的$extend_columns变量的relative字段下的data配置数组添加'xxx' => 活动唯一权值
 * 2.在当前文件所在目录下创建xxx_event.php，按example_event.php中的配置信息写相应配置信息 注： 1中relative中指定的中文活动名应与xxx_event.php中的中文名称一致
 * 3.访问相应路径下的本代码，并传入?f=xxx即可
 *
*/

require_once dirname(__FILE__).'/../lib/config.php';
require_once dirname(__FILE__).'/../lib/mysql.php';
include dirname(__FILE__).'/../pages/quest_activity_center_extend.php';
include './events/config.php';  //使用前添加 define('ROOT_PATH', '/Users/stauff/xxd');


$f = $_GET['f'];

if(isset($f) && !empty($f)){

	$file_name = $f.'_event.php';
	require("./events/".$file_name); //加载配置文件
	$name = $config['name']; //活动名称
	$key = $config['key']; //活动标识
	$key_name = $config['key_name']; //活动单一名称，如等级，战力等

	// 1.活动中心插入记录
	$event_key = 'event_'.$key.'_awards';
	$event_center_sql = 'INSERT INTO `quest_activity_center`(`name`,`relative`,`sign`) VALUES(\''.$name.'\','.array_search($name, $extend_columns['relative']['data']).
												',\''.strtoupper($event_key).'\');';
	global $db_config;
	$db = db_connect();

	db_execute($db, $event_center_sql); //在活动中心插入记录

	//2.创建活动奖励配置表的脚本
	$table_sql = file_get_contents('./events/templates/event_awards_sql_template.tpl');
	file_put_contents(ROOT_PATH.'/database/servers/game_server/'.date("Y-m-d").'-max.php', str_replace(array('{key_val}','{name_val}','{title_val}'), array($key, $key_name,$name), $table_sql));
	chmod(ROOT_PATH.'/database/servers/game_server/'.date("Y-m-d").'-max.php',0666);

	//3.在pages目录下创建配置文件和扩展配置文件
	$page_config = 'events_'.$key.'_awards.php';
	$page_extend_config = 'events_'.$key.'_awards_extend.php';

	$page_config_tpl = file_get_contents('./events/templates/page_config.tpl');
	$page_config_extend_tpl = file_get_contents('./events/templates/page_config_extend.tpl');

	file_put_contents('../pages/'.$page_config, str_replace(array('{name_val}','{pt_val}','{key_val}'), array($name,$key,$key_name), $page_config_tpl));
	file_put_contents('../pages/'.$page_extend_config, $page_config_extend_tpl);


	
	//4.event_dat下建立go文件内容
	$tf_val = getTuoFeng($key);
	$go_contents = file_get_contents('./events/templates/event_dat_go_file.tpl');
	$contents = str_replace(array('{tf_key}','{pt_val}','{name_val}'), array($tf_val, $key, $name), $go_contents);
	file_put_contents(ROOT_PATH.'/server/src/game_server/dat/event_dat/event_'.$key.'.go', $contents);
	chmod(ROOT_PATH.'/server/src/game_server/dat/event_dat/event_'.$key.'.go',0666);


	//5.添加添加json设置
	$json_str = <<<EOL
	    "{$tf_val}":{<br />
        "StartUnixTime":-1,<br />
        "EndUnixTime":-1,<br />
        "DisposeUnixTime":-1,<br />
        "LTitle":"",<br />
        "RTitle":"",<br />
        "Content":"",<br />
        "List":[<br /><br />
            {<br />
                "Require{$tf_val}":0,<br />
                "Ingot":0,<br />
                "Coin":0,<br />
                "Item1Id":0,<br />
                "Item1Num":0,<br />
                "Item2Id":0,<br />
                "Item2Num":0,<br />
                "Item3Id":0,<br />
                "Item3Num":0,<br />
                "Item4Id":0,<br />
                "Item4Num":0,<br />
                "Item5Id":0,<br />
                "Item5Num":0<br />
            }<br /><br />
        ]<br />
    }<br />
EOL;

	//显示手动需要输入的内容
$up_key = strtoupper($event_key);
	echo <<<EOL
接下来需要做的有：<br />
1.在server/src/game_server/dat/event_dat/event_dat.go的func Load(db *mysql.Connection)中添加   loadEvents{$tf_val}(db)<br /><br />
2.在system/index.php的运营链接数组设置中，添加    array('text' => '{$name}', 'type' => 'link', 'id' => 'events_{$key}_awards', 'ids' => array()),<br /><br />
3.在数据库脚本中修改新生成的以_max结尾的数据库脚本名称<br /><br />
4.在event.json中添加<br />
	{$json_str}<br /><br />
5.在module/event/event_config.go中的EventConfigExtend结构体定义中添加{$tf_val} *event_dat.Events{$tf_val}Ext<br /><br />
6.继续在event_config.go的LoadEventExtend方法中添加<br />
	event_dat.LoadEvents{$tf_val}(eventExt.{$tf_val}.List)<br />
	event_dat.LoadEventCenterExt(eventExt.{$tf_val}.StartUnixTime, eventExt.{$tf_val}.EndUnixTime, eventExt.{$tf_val}.DisposeUnixTime, event_dat.{$up_key})           //{$name}<br />
EOL;
}else{
	printf("缺少配置文件信息");
}

function getTuoFeng($str){
	$arr = explode('_', $str);
	foreach ($arr as &$value) {
		$value = ucfirst($value);
	}
	return implode('', $arr);
}

?>