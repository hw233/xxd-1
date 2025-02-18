<?php 
$db_config = array(
  'local_game' => array(
    'host' => '127.0.0.1',
    'user' => 'lms',
    'pass' => '123456',
    'name' => 'mobile_xxd',
    'port' => '3306',
    'server' => 'game_server',
  ),
);

/*
 * 有部分 table 存在 不同发型版本数值存在差异，那么这种特殊的表在 vendor_special_table 中配置
 * 假设在default分支倒出的数据会带上
 * $this->AddSQL("create table other_table ...");
 *
 * if ($branch != $$branch != 'soha' && $branch != 'tw') {
 * 	$this->AddSQL("create table foo_table ...");
 * }
 * 假设在 soha 分支导出会变成
 * if ($branch == 'soha') {
 * 	$this->AddSQL("create table foo_table ...");
 * }
 */
$vendor_special_table = array(
	'foo_table' => array('soha','tw'),
);

// eg:
//$vendor_special_table = array(
//	'vip_level' => array('soha','tw', 'default' ),
//	'vip_levelup_gift' => array('soha',),
//	'vip_privilege' => array('soha',),
//	'vip_privilege_config' => array('soha',),
//);


if (file_exists(dirname(__FILE__)."/__config.php"))
	require_once(dirname(__FILE__)."/__config.php");
?>
