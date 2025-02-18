<?php
include "common_links.php";

$extend_columns = array(
/*   '字段' => 配置 */
	'child_type' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array(),
		'range' =>array('params' => array()),
	),
	'child_kind' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array(),
		'range' =>array('params' => array()),
	),

	'quality' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array(),
		'range' =>array('params' => array()),
	),
	'jump_attack' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array('否','是'),
	),
	'auto_learn_level' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array('否','是'),
	),
	'parent_skill_id' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array(),
		'range' =>array('params' => array()),
	),
    'cheat_id' => array(
        'editor' => array('params' => array()),
        'render' => array('params' => array()),
        'data' => array(),
        'range' =>array('params' => array()),
    ),
	'display_param' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => array(),
		'range' =>array('params' => array()),
		'handle' => true,
	),
	'target' => array(
		'editor' => array('params' => array()),
		'render' => array('params' => array()),
		'data' => $skill_target_type,
	),
);

$parentSkills = db_query($db, "select * from `skill` where `type` = 1 order by `role_id`;");
foreach ($parentSkills as $value) {
	$parentSkill[$value['id']] = $value['name'];
}


$all_item_cheats = db_query($db, "select `id`, `name` from `item` where `type_id` = 17");
foreach ($all_item_cheats as $value) {
    $all_item_cheat[$value['id']] = $value['name'];
}

function handle_display_param($content){
	global $display_params;
	$items = explode(',', $content);
	$result = 0;
	foreach ($items as $value) {
		$search = array_search($value, $display_params);
		if ($search === false) {
			return false;
		}
		$result += $search;
	}
	return $result;
}

function range_child_kind(){
	global $skillKind;
	return $skillKind;
}
function range_display_param(){
	global $display_params;
	$param_temp = $display_params;
	$param_temp[0] = '无';
	return $param_temp;
}
function range_child_type(){
	global $skillTypes;
	return $skillTypes;
}
function range_quality(){
	global $qualityTypes;
	return $qualityTypes;
}
function range_parent_skill_id(){
	global $parentSkill;
	$parent_temp = $parentSkill;
	$parent_temp[0] = '无';
	return $parent_temp;
}

function range_cheat_id(){
    global $all_item_cheat;
    $cheat_temp = $all_item_cheat;
    $cheat_temp[0] = '无';
    return $cheat_temp;
}

function render_child_type($column_name, $column_val, $row, $data){
	global $skillTypes;
	return $skillTypes[$row['child_type']];
}

function editor_child_type($column_name, $column_val, $row, $data){
	global $skillTypes;
	return html_get_select($column_name,$skillTypes,$column_val);
}

function render_child_kind($column_name, $column_val, $row, $data){
	global $skillKind;
	return $skillKind[$row['child_kind']];
}

function editor_child_kind($column_name, $column_val, $row, $data){
	global $skillKind;
	return html_get_select($column_name,$skillKind,$column_val);
}

function render_quality($column_name, $column_val, $row, $data){
	global $qualityTypes;
	return $qualityTypes[$row['quality']];
}

function editor_quality($column_name, $column_val, $row, $data){
	global $qualityTypes;
	return html_get_select($column_name,$qualityTypes,$column_val);
}

function render_jump_attack($column_name, $column_val, $row, $data){
	return $data[$column_val];
}

function editor_jump_attack($column_name, $column_val, $row, $data){
	return html_get_select($column_name,$data,$column_val);
}

function render_auto_learn_level($column_name, $column_val, $row, $data){
	return $data[$column_val];
}

function editor_auto_learn_level($column_name, $column_val, $row, $data){
	return html_get_select($column_name,$data,$column_val);
}

function render_target($column_name, $column_val, $row, $data){
	return $data[$column_val];
}

function editor_target($column_name, $column_val, $row, $data){
	return html_get_select($column_name,$data,$column_val);
}

function render_parent_skill_id($column_name, $column_val, $row, $data){
	global $parentSkill;
	$html = '';
	if (isset($parentSkill[$row['parent_skill_id']])){
		$html .= $parentSkill[$row['parent_skill_id']];
	}
	return $html;
}

function editor_parent_skill_id($column_name, $column_val, $row, $data){
	global $parentSkills;
	$code = '';
	$code .= '<select name="parent_skill_id[]" >';
	$code .= '<option value="0" selected="selected">无</option>';
	if ($row != null) {
		foreach ($parentSkills as $value){
			if ($value['id'] == $row['parent_skill_id']) {
				$code .= '<option value="'.$value['id'].'"  selected="selected">'.$value['name'].'</option>';
			} else {
				$code .= '<option value="'.$value['id'].'" >'.$value['name'].'</option>';
			}
		}
	} else {
		foreach ($parentSkills as $value){
			$code .= '<option value="'.$value['id'].'" >'.$value['name'].'</option>';
		}
	}
	$code .= '</select>';
	return $code;
}

function render_cheat_id($column_name, $column_val, $row, $data){
    global $all_item_cheat;
    $html = '';
    if (isset($all_item_cheat[$row['cheat_id']])){
        $html .= $all_item_cheat[$row['cheat_id']];
    }
    return $html;
}

function editor_cheat_id($column_name, $column_val, $row, $data){
    global $all_item_cheats;
    $code = '';
    $code .= '<select name="cheat_id[]" >';
    $code .= '<option value="0" selected="selected">无</option>';
    if ($row != null) {
        foreach ($all_item_cheats as $value){
            if ($value['id'] == $row['cheat_id']) {
                $code .= '<option value="'.$value['id'].'"  selected="selected">'.$value['name'].'</option>';
            } else {
                $code .= '<option value="'.$value['id'].'" >'.$value['name'].'</option>';
            }
        }
    } else {
        foreach ($all_item_cheats as $value){
            $code .= '<option value="'.$value['id'].'" >'.$value['name'].'</option>';
        }
    }
    $code .= '</select>';
    return $code;
}

 function render_display_param($column_name, $column_val, $row, $data){
	global $display_params;
	$code  = '';
	foreach ($display_params as $key => $value) {
		if (($row['display_param']&$key) == $key) {
			$code .= $value.'<br>';
		}
	}
 	return $code;
 }

 function editor_display_param($column_name, $column_val, $row, $data){
	global $display_params;
	$code  = '';
 	if ($row != null) {
 		$drama_mode = 0;
		foreach ($display_params as $key => $value) {
			if (($row['display_param']&$key)==$key) {
				$code .= '<input type="checkbox" name="display_param_editor" value="'.$key.'" checked="true">'.$value.'<br>';
			$drama_mode += $key;
			}else{
				$code .= '<input type="checkbox" name="display_param_editor" value="'.$key.'">'.$value.'<br>';
			}
 		}
 		$code .= '<input type="hidden" name="display_param[]" value="'.$drama_mode.'" />';
 	} else {
		foreach ($display_params as $key => $value) {
			$code  .= '<input type="checkbox" name="display_param_editor" value="'.$key.'">'.$value.'<br>';
		}
		
 		$code .= '<input type="hidden" name="display_param[]" value="0" />';
 	}
 	return $code;
}

function jsFunction($params) {
	
	$html = '$("[name=\'display_param_editor\']").click( function(){
		var s = 0;
		$(this).parent().children("input[name=\'display_param_editor\']").each(function(){ //由于复选框一般选中的是多个,所以可以循环输出
			if($(this).attr("checked")){
				s += parseInt($(this).val());
			}
		});
		$(this).parent().children("input:hidden").val(s);
		
	});';
	return $html;
}

function foot() {
	require dirname(__FILE__).'/skill_editor.php';
	require dirname(__FILE__).'/skill_info_editor.php';
}

function skill_opera($row) {
	return '<a href="javascript:;" onclick="open_editor(\''.$row['name'].'\', \''.$row['info'].'\', \''.$row['id'].'\', false)">配置绝招</a> | ';
}

function skill_info($row) {
	return '<a href="javascript:;" onclick="edit_skill_info(\''.$row['id'].'\')">绝招描述</a>';
}

function sql_where($params) {
	return " where `type` =1 and `role_id` = -2 ORDER BY `required_level`,`parent_skill_id` ASC";
}

function sql_insert($params) {
	return "`type` = 1, `role_id` = -2";
}

?>
