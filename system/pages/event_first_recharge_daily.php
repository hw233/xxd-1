<?php

$pconfig = array(
	'title'   => '每日首冲奖励',
	'table'   => 'event_first_recharge_daily',
	'links'   => array(),
	
	'columns' => array(
		array('name' => 'require_day', 'text' => '索引天数', 'width' => '80px'),
		array('name' => 'ingot', 'text' => '奖励元宝', 'width' => '80px'),
		array('name' => 'coins', 'text' => '奖励铜钱', 'width' => '80px'),
		array('name' => 'heart', 'text' => '奖励爱心', 'width' => '80px'),
		array('name' => 'item1_id', 'text' => '物品1', 'width' => '80px'),
		array('name' => 'item1_num', 'text' => '物品1数量', 'width' => '80px'),
		array('name' => 'item2_id', 'text' => '物品2', 'width' => '80px'),
		array('name' => 'item2_num', 'text' => '物品2数量', 'width' => '80px'),
		array('name' => 'item3_id', 'text' => '物品3', 'width' => '80px'),
		array('name' => 'item3_num', 'text' => '物品3数量', 'width' => '80px'),
		array('name' => 'item4_id', 'text' => '物品4', 'width' => '80px'),
		array('name' => 'item4_num', 'text' => '物品4数量', 'width' => '80px'),
		array('name' => 'item5_id', 'text' => '物品5', 'width' => '80px'),
		array('name' => 'item5_num', 'text' => '物品5数量', 'width' => '80px'),

	),
	
	'where' 		=> 'sql_where',
	'js' 			=> 'js_function',
);

function sql_where(){
	return ' ORDER BY `require_day` ASC ';
}

?>