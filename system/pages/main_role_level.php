<?php

function location($params){
  global $db;
  $html = '';
  $sql = "select `id`, `name` from role where id = {$params['m']}";
  $role = db_query($db, $sql);
  if (count($role) == 0) {
    return $html;
  }

  $html = '<a href="?p=role">'.$role[0]['name'].'</a> -> ' . $html;

  return $html;
}

function sql_where($params) {
  return "where `role_id`={$params['m']} order by `level`";
}

function sql_insert($params) {
  return "`role_id` = {$params['m']}";
}


$mainRoleId = array(1, 2);

$pconfig = array(
  'title'   => '角色等级数据',
  'table'   => 'role_level',
  'location'=> 'location',
  'links'   => array(
    array('text' => '玩家角色数据', 'id' => 'role'),
    array('text' => '敌人角色数据', 'id' => 'enemy_role'),
    // array('text' => '主角声望', 'id' => 'fame_level'),
  ),
  'columns' => array(
    array('name' => 'level', 'text' => '等级', 'width' => '30px'),
    array('name' => 'health',   'text' => '生命', 'width' => '60px'),
    array('name' => 'attack',   'text' => '攻击', 'width' => '60px'),
    array('name' => 'defence',   'text' => '防御', 'width' => '60px'),
    array('name' => 'cultivation',   'text' => '内力', 'width' => '60px'),
    array('name' => 'speed',   'text' => '速度', 'width' => '60px'),
    array('name' => 'critial',   'text' => '暴击%', 'width' => '60px'),
    array('name' => 'block',   'text' => '格挡%', 'width' => '60px'),
    array('name' => 'hit',   'text' => '命中%', 'width' => '60px'),
    array('name' => 'dodge',   'text' => '闪避%', 'width' => '60px'),
    array('name' => 'critial_hurt',   'text' => '必杀%', 'width' => '60px'),
    array('name' => 'sleep',  'text' => '睡眠抗性%', 'width' => '60px'),
    array('name' => 'dizziness',  'text' => '眩晕抗性%', 'width' => '60px'),
    array('name' => 'random',  'text' => '混乱抗性%', 'width' => '60px'),
    array('name' => 'disable_skill',  'text' => '封魔抗性%', 'width' => '60px'),
    array('name' => 'poisoning',  'text' => '中毒抗性%', 'width' => '60px'),
  ),
  'where'   => 'sql_where',
  'insert'  => 'sql_insert',
  "pagesize" => 9999,
);


if (in_array($_GET['m'], $mainRoleId)) {
	$pconfig['columns']	= array_merge($pconfig['columns'], array(
    array('name' => 'init_power',   'text' => '初始精气', 'width' => '60px'),
    array('name' => 'max_power',   'text' => '精气上限', 'width' => '60px'),
	));
}

$pconfig['columns'] = array_merge($pconfig['columns'], array(
  array('name' => 'sunder_max_value', 'text' => '护甲上限','width' => '60px'),
  array('name' => 'sunder_hurt_rate', 'text' => '破甲起始百分比','width' => '60px'),
  array('name' => 'sunder_end_hurt_rate', 'text' => '破甲后百分比','width' => '60px'),
  array('name' => 'sunder_end_defend_rate', 'text' => '破甲后减防百分比','width' => '60px', 'default' => '150'),
  array('name' => 'sunder_round_num', 'text' => '破甲持续回合','width' => '60px'),	
  array('name' => 'sunder_dizziness', 'text' => '破甲眩晕回合','width' => '60px',),
));
?>
