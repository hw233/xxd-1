<?php
$config = array(

	array('const',
		'Item_Mission_Key_Id' => 262,  // 模板数据库中光明钥匙的ID
                'Item_Ghost_Crystal_Id' => 796, // 模板数据中魂侍水晶ID
	),

	array('const',
		'ITEM_DRIVING_SWORD_CLOUD_STONE' => 727, //云海御剑石符
	),
	
	array('const',
		'BATCH_USE_MAX_NUM' => 10, //批量使用物品的数量最大值
	),

	array( 'const',
		'MAX_BAG_NUM' => 48*2,  //背包容量
		'MAX_ITEM_NUM' => 74, //背包容量+装备数量+回购栏
		'MAX_EQUIPMENT_NUM' => 20, //最大装备数量
		'EQUIPMENT_NUM_EVERYBODY' => 4, //每个人的装备数量
		'BUY_BACK_NUM' => 6, //回购栏数量
		'ITEM_STATE_SOLD' => 1, //处于已出售状态
	),

	array( 'const',
		'TYPE_SPECIAL_MATERIAL' => 2,  //材料
		'TYPE_WEAPON'           => 3,  //武器
		'TYPE_CLOTHES'          => 4,  //战袍
		'TYPE_SHOE'             => 5,  //靴子
		'TYPE_ACCESSORIES'      => 6,  //饰品
		'TYPE_BATTLE_PROPS'            => 8,  //战斗道具
		'TYPE_CHEST'            => 9,  //礼包
		'TYPE_RESOURCE'         => 10, //资源
		'TYPE_GHOST_FRAGMENT'   => 13, //魂侍碎片

		'TYPE_BATTLE_PET'	=> 11, // 灵宠契约球
		'TYPE_COST_PROPS'	=> 15, // 消耗道具
		'TYPE_FASHION'	=> 16, // 时装
		'TYPE_CHEAT'	=> 17, // 绝招秘籍
		'TYPE_QUEST'	=> 19, // 喜好品
		'TYPE_DRAGON_BALL'	=> 20, // 龙珠
		'TYPE_ACT_REFLECT'	=> 21, // 秘宝
		'TYPE_EVENT' => 22, // 活动道具
	),

	/*可使用物品*/
	array( 'const',
		'ITEM_JINGYANG'        => 243, //经验
		'ITEM_ZHENQILONGZHU'        => 264, //真气龙珠
		'ITEM_YINGJIEGUOSHI'        => 263, //影界果实
		'ITEM_LONGBI'               => 270, //龙币
		'ITEM_BLUE_CRYSTAL'         => 231, //蓝色结晶
		'ITEM_PURPLE_CRYSTAL'       => 232, //紫色结晶
		'ITEM_GOLDEN_CRYSTAL'       => 233, //金色结晶
		'ITEM_ORANGE_CRYSTAL'       => 234, //橙色结晶
		'ITEM_WEAPON_FRAGMENT'      => 235, //武器碎片
		'ITEM_CLOTHES_FRAGMENT'     => 236, //护甲碎片
		'ITEM_SHOE_FRAGMENT'        => 237, //靴子碎片
		'ITEM_ACCESSORIES_FRAGMENT' => 238, //饰品碎片
		'ITEM_SWORD_SOUL_FRAGMENT'  => 269, //剑心碎片
		'ITEM_BONE' =>  682, //兽骨
		'ITEM_HALLOW' =>  683, //圣器
		'ITEM_SWORD_DRIVING_FLAG'  => 792, //混云幡
	),
	
	/* 资源物品 */
	array( 'const',
		'ITEM_PHYSICAL' => 248, //体力
		'ITEM_INGOT' => 242, //元宝
		'ITEM_COIN'  => 244, //铜钱
		'ITEM_HEART' => 247, //爱心	
	),

	/*物品品质*/
	array( 'const',
		'ITEM_QUALITY_GREEN' => 0, //绿
		'ITEM_QUALITY_BLUE' => 1,  //蓝
		'ITEM_QUALITY_PURPLE' => 2,//紫
		'ITEM_QUALITY_GOLD' => 3,  //金
		'ITEM_QUALITY_ORANGE' => 4,//橙
	),

	/*物品属性*/
	array( 'const',
		'ATTRIBUTE_NULL'           => 0,   //无
		'ATTRIBUTE_ATTACK'         => 1,   //攻击
		'ATTRIBUTE_DEFENCE'        => 2,   //防御
		'ATTRIBUTE_HEALTH'         => 3,   //生命
		'ATTRIBUTE_SPEED'          => 4,   //速度 
		'ATTRIBUTE_CULTIVATION'    => 5,   //内力
		'ATTRIBUTE_HIT_LEVEL'      => 6,   //命中等级
		'ATTRIBUTE_CRITICAL_LEVEL' => 7,   //暴击等级
		'ATTRIBUTE_BLOCK_LEVEL'    => 8,   //格挡等级
		'ATTRIBUTE_DESTROY_LEVEL'  => 9,   //破击等级
		'ATTRIBUTE_TENACITY_LEVEL' => 10,  //韧性等级
		'ATTRIBUTE_DODGE_LEVEL'    => 11,  //闪避等级
		'ATTRIBUTE_NUM'            => 11,  //属性数目
	),
	
	/*物品附加属性随机单位*/
	array( 'const',
		'ATTRIBUTE_RANDOM_UNIT_ATTACK'         => 10,   //攻击
		'ATTRIBUTE_RANDOM_UNIT_DEFENCE'        => 5,   //防御
		'ATTRIBUTE_RANDOM_UNIT_HEALTH'         => 50,   //生命
		'ATTRIBUTE_RANDOM_UNIT_SPEED'          => 10,   //速度 
		'ATTRIBUTE_RANDOM_UNIT_CULTIVATION'    => 10,   //内力
		'ATTRIBUTE_RANDOM_UNIT_HIT_LEVEL'      => 5,   //命中等级
		'ATTRIBUTE_RANDOM_UNIT_CRITICAL_LEVEL' => 5,   //暴击等级
		'ATTRIBUTE_RANDOM_UNIT_BLOCK_LEVEL'    => 5,   //格挡等级
		'ATTRIBUTE_RANDOM_UNIT_DESTROY_LEVEL'  => 5,   //破击等级
		'ATTRIBUTE_RANDOM_UNIT_TENACITY_LEVEL' => 5,  //韧性等级
		'ATTRIBUTE_RANDOM_UNIT_DODGE_LEVEL'    => 5,  //闪避等级
	),

	/*商品相关*/
	array( 'const',
		'SELL_DISCOUNT' => 0.3, //卖物品折扣
		'SELL_EQUIP_DISCOUNT' => _S(1.0, 1.0, 0.8, 1.0), //出售装备折扣
		'SELL_EQUIP_RECAST_DISCOUNT' => 0.3, //出售装备重铸部分折扣
	),

	/*装备相关*/
	array( 'const',
		'EQUIPMENT_MAIN_ROLE_ID' => -1, //装备角色为主角
	),
	
	/*装备精炼等级*/
	array( 'const',
		'REFINE_FAIL_MAKEUP_PROBABILITY' => 5, //精炼失败补偿概率 百分比
		'EQUIPMENT_REFINE_LEVEL0' => 0,
		'EQUIPMENT_REFINE_LEVEL1' => 1,
		'EQUIPMENT_REFINE_LEVEL2' => 2,
		'EQUIPMENT_REFINE_LEVEL3' => 3,
		'EQUIPMENT_REFINE_LEVEL4' => 4,
		'EQUIPMENT_REFINE_LEVEL5' => 5,
		'EQUIPMENT_REFINE_LEVEL6' => 6,
		'EQUIPMENT_REFINE_LEVEL7' => 7,
		'EQUIPMENT_REFINE_LEVEL8' => 8,
		'EQUIPMENT_REFINE_LEVEL9' => 9,
		'EQUIPMENT_REFINE_LEVEL10' => 10,
		'MAX_EQUIPMENT_REFINE_LEVEL' => 10, // 装备精炼的最大等级
		'BATCH_REFINE_TIMES' => 5, // 批量强化的默认次数
	),

	array('const',
	    'DECOMPOSE_COINS_REFUND_RATE' => 0.3,	    /*装备分解铜币返还比例*/
	    'DECOMPOSE_COINS_REFINE_RATE' => _S(1.0, 1.0, 0.8, 1.0),  //装备分解精炼铜钱返还比例
	),
	
	/*装备重铸*/
	array( 'const',
		'EQUIPMENT_RECAST_RANDOM_ATTR_NUM' => 3,
	),
	
	/* 指向面板 */
	array( 'const',
		'PANEL_NULL'                => 0, // 无
		'PANEL_REALM'               => 1, // 境界升级
	 	'PANEL_GHOST_EXCHANGE'      => 2, // 魂侍兑换
		'PANEL_GHOST_TRAIN'         => 3, // 魂侍培养
		'PANEL_SWORD_SOUL_EXCHANGE' => 4, // 剑心兑换
		'PANEL_BATTLE_PET_INFO'     => 5, // 灵宠信息
		'PANEL_GHOST'               => 6, // 魂侍首页
		'PANEL_PET_GRID_UPGRADE' =>7, //指向面板	
		'PANEL_TOTEM'				=> 8, // 阵印
		'PANEL_AWAKEN'              => 9, // 觉醒
	),

	/* 功能反射 */
	array( 'const',
		'ITEM_ACTREF_NON'             => 0, //无
		'ITEM_ACTREF_OPEN_CORNUCOPIA' => 1, //开启聚宝盆
	),

	/* 消耗道具类型 */
	array( 'const',
		'COST_ITEM_EXP'                => 0, // 经验
		'COST_ITEM_PHY'                => 1, // 体力
		'COST_ITEM_SHP'                => 2, // 友情
	),	

	/* 操作player_Item表的数据类型 */
	array('const',
		'MODIFY_DELETE'		=>	0,	//删除
		'MODIFY_UPDATE'		=>	1,	//更新
		'MODIFY_INSERT'		=>	2,	//插入
	),

	array('const',
		'CONSUME_DRAGON_BALL_NUM' => 7, //龙珠一次消耗数量	
	),

	array('const',
		'CORNUCOPIA_MAX_DAILY_USING_AMOUNT' => 1, //聚宝盆每天最多使用次数
	),
	array('const',
		'STEALDBOOK_HAVED' => 1,  		//以前拥有过
		'STEALDBOOK_HAVING' => 2, 		//现在拥有,但未激活
		'STEALDBOOK_ACTIVATION' => 3, 	//激活
	),

	array('const',
		'STEALDBOOK_TYPE_ROLES' => 1,  		//伙伴
		'STEALDBOOK_TYPE_GHOSTS' => 2, 		//魂侍
		'STEALDBOOK_TYPE_SWORDSOULS' => 3, 	//剑心
		'STEALDBOOK_TYPE_PETS' => 4, 		//灵宠
		'STEALDBOOK_TYPE_TOTEMS' => 6, 	    //阵印
		'STEALDBOOK_TYPE_NOEQUIPMENTS' => 7, //资源
		'STEALDBOOK_TYPE_BATTLETOOLS' => 8,  //战斗道具

		'STEALDBOOK_TYPE_WEAPON' => 9,  //武器
		'STEALDBOOK_TYPE_CLOTHES' => 10,  //装备
		'STEALDBOOK_TYPE_SHOE' => 11,  //鞋
		'STEALDBOOK_TYPE_ACCESSORIES' => 12,  //装饰

	),
	array('const',
		"CLIQUE_CONTRIBUTE_ID" => 793, //帮派贡献ID
		)
);
?>
