<?php
require_once dirname(__FILE__).'/../lib/global.php';
$links = array(
	array('text' => '主角招式', 'id' => 'skill'),
	array('text' => '伙伴招式', 'id' => 'skill_buddy'),
);
$sql = 'SELECT `id`, `name` FROM `role` WHERE `type`=2;';
$rows = db_query($db, $sql);
foreach ($rows as $row) {
	$links[] = array('text' => $row['name'], 'id' => 'skill_buddy&m='.$row['id']);
}
$links[] = array('text' => '敌人招式', 'id' => 'skill_enemy');
$links[] = array('text' => '绝招训练消耗', 'id' => 'skill_training_cost');

?>
