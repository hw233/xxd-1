<?php
	require_once dirname(__FILE__).'/../lib/global.php';

	// 提交
 	if (isset($_POST['config'])
 		&& isset($_POST['boss_id'])) {


 		$sql = "select * from enemy_boss_script where boss_id='{$_POST['boss_id']}'";
 		$rows = db_query($db, $sql);
 		
 		if (count($rows)>0) {
 			$sql = "update enemy_boss_script set config='{$_POST['config']}' where boss_id='{$_POST['boss_id']}'";
 		} else {
 			$sql = "insert enemy_boss_script set config='{$_POST['config']}',boss_id='{$_POST['boss_id']}'";
 		}
 		db_query($db, $sql);
 	} else if (isset($_GET['boss_id']) && $_GET['boss_id']>0) {
		$sql = "select config from enemy_boss_script where boss_id='{$_GET['boss_id']}'";
 		$rows = db_query($db, $sql);
 		if (count($rows)>0)
	 		echo $rows[0]['config'];
	 	else
	 		echo "[]";
 	}
?>