var hard_level_data = {
		/**
	 * 0 : id, smallint, 
	 * 1 : mission_level_lock, int, 区域关卡功能权值
	 * 2 : desc, varchar, 关卡描述
	 * 3 : town_id, smallint, 城镇ID
	 * 4 : hard_level_lock, int, 难度关卡权值 
	 */

	Id : 0,
	Mission_level_lock : 1,
	Desc : 2,
	Town_id : 3,
	Hard_level_lock : 4,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 100110 /*[1]*/, "竹林里的竹子都成精了。" /*[2]*/, 1 /*[3]*/, 0 /*[4]*/],
		[2 /*[0]*/, 110130 /*[1]*/, "拥有摄人魂魄之能的灯笼怪。" /*[2]*/, 1 /*[3]*/, 100100 /*[4]*/],
		[3 /*[0]*/, 120140 /*[1]*/, "原来剧毒臭泥是吸收了各种腐化的气息后从地底逃窜到人间的。" /*[2]*/, 1 /*[3]*/, 100110 /*[4]*/],
		[4 /*[0]*/, 130150 /*[1]*/, "虽然炎龙尚未被阴影吞噬，但是在腐烂的地底，炎龙早已不是曾经的炎龙。" /*[2]*/, 1 /*[3]*/, 100120 /*[4]*/],
		[5 /*[0]*/, 140150 /*[1]*/, "上古的剑灵恐怕做梦也不会想到，自己的肉身会被魔物所占据。" /*[2]*/, 1 /*[3]*/, 100130 /*[4]*/],
		[6 /*[0]*/, 150170 /*[1]*/, "想不到一个小小的牢头也是大有来头的。" /*[2]*/, 2 /*[3]*/, 100140 /*[4]*/],
		[7 /*[0]*/, 160170 /*[1]*/, "野猪王充满了戾气与怨恨，被阴影侵蚀堕入深渊。" /*[2]*/, 2 /*[3]*/, 100150 /*[4]*/],
		[8 /*[0]*/, 170170 /*[1]*/, "深渊中的火麒麟被控制后脾气变的更加暴躁。" /*[2]*/, 2 /*[3]*/, 100160 /*[4]*/],
		[9 /*[0]*/, 180170 /*[1]*/, "为了除魔而进入深渊的地藏王也被阴影所侵蚀了。" /*[2]*/, 2 /*[3]*/, 100170 /*[4]*/],
		[10 /*[0]*/, 190170 /*[1]*/, "四大魔头之一奸奇的罪恶之源" /*[2]*/, 2 /*[3]*/, 100180 /*[4]*/],
		[11 /*[0]*/, 200170 /*[1]*/, "想不到古代武圣的肉身也被魔物侵占了" /*[2]*/, 4 /*[3]*/, 100190 /*[4]*/],
		[12 /*[0]*/, 210170 /*[1]*/, "聚集了太多怨气而化为妖魔的老树" /*[2]*/, 4 /*[3]*/, 100200 /*[4]*/],
		[13 /*[0]*/, 220170 /*[1]*/, "本是昆墟的守护，却在昆墟沦陷时一同堕入了深渊" /*[2]*/, 4 /*[3]*/, 100210 /*[4]*/],
		[14 /*[0]*/, 230170 /*[1]*/, "经过千年修炼的一条电鳗，可是不小心被阴影腐蚀了" /*[2]*/, 4 /*[3]*/, 100220 /*[4]*/],
		[15 /*[0]*/, 240170 /*[1]*/, "本是人间暴君，死后依旧本性不改" /*[2]*/, 4 /*[3]*/, 100230 /*[4]*/],
		[16 /*[0]*/, 250170 /*[1]*/, "三位上古仙灵中的飞羽肉身也已经沦陷了" /*[2]*/, 5 /*[3]*/, 100240 /*[4]*/],
		[17 /*[0]*/, 260170 /*[1]*/, "四大魔头之一色孽的罪恶之源" /*[2]*/, 5 /*[3]*/, 100250 /*[4]*/],
		[18 /*[0]*/, 270170 /*[1]*/, "操控风的大魔头，不知什么原因甘于屈居在徐福之下" /*[2]*/, 5 /*[3]*/, 100260 /*[4]*/],
		[19 /*[0]*/, 280170 /*[1]*/, "四大魔头之一纳垢的罪恶之源" /*[2]*/, 5 /*[3]*/, 100270 /*[4]*/],
		[20 /*[0]*/, 290170 /*[1]*/, "曾是著名方士，率众出海采仙药，一去不返" /*[2]*/, 5 /*[3]*/, 100280 /*[4]*/],
		[21 /*[0]*/, 300170 /*[1]*/, "四大魔头之一恐虐的罪恶之源" /*[2]*/, 6 /*[3]*/, 100290 /*[4]*/],
		[22 /*[0]*/, 310170 /*[1]*/, "藏匿在狂风巨浪的海岸边可怕的海妖" /*[2]*/, 6 /*[3]*/, 100300 /*[4]*/],
		[23 /*[0]*/, 320170 /*[1]*/, "带着不甘的第六天魔王织田信长" /*[2]*/, 6 /*[3]*/, 100310 /*[4]*/],
		[24 /*[0]*/, 330170 /*[1]*/, "天皇丑恶内心的罪恶之源" /*[2]*/, 6 /*[3]*/, 100320 /*[4]*/],
		[25 /*[0]*/, 340170 /*[1]*/, "死而不僵的骷髅将军" /*[2]*/, 6 /*[3]*/, 100330 /*[4]*/],
		[26 /*[0]*/, 350170 /*[1]*/, "一把马战用的关刀在虐杀手里平地上也能如臂使指" /*[2]*/, 7 /*[3]*/, 100340 /*[4]*/],
		[27 /*[0]*/, 360170 /*[1]*/, "龙虎门掌门，拳掌功夫相当了得" /*[2]*/, 7 /*[3]*/, 100350 /*[4]*/],
		[28 /*[0]*/, 370170 /*[1]*/, "先天的剑阵也堕入了魔道" /*[2]*/, 7 /*[3]*/, 100360 /*[4]*/],
		[29 /*[0]*/, 380170 /*[1]*/, "扫地的无名老僧武功竟已入化境" /*[2]*/, 7 /*[3]*/, 100370 /*[4]*/],
		[30 /*[0]*/, 390170 /*[1]*/, "手执狂刀似乎有着摧毁一切的无穷力量" /*[2]*/, 7 /*[3]*/, 100380 /*[4]*/],
		[31 /*[0]*/, 400170 /*[1]*/, "屠魔虐杀吸收了阴影之力，准备卷土重来" /*[2]*/, 8 /*[3]*/, 100390 /*[4]*/],
		[32 /*[0]*/, 410170 /*[1]*/, "由尸体转化而成的血咒死士拥有非常强大的力量" /*[2]*/, 8 /*[3]*/, 100400 /*[4]*/],
		[33 /*[0]*/, 420170 /*[1]*/, "堕魔是由阴影聚合合成，不是普通阴影能够比拟的" /*[2]*/, 8 /*[3]*/, 100410 /*[4]*/],
		[34 /*[0]*/, 430170 /*[1]*/, "血吼被阴影影响后变的更加狂暴" /*[2]*/, 8 /*[3]*/, 100420 /*[4]*/],
		[35 /*[0]*/, 440170 /*[1]*/, "忆境冥灵吸收了阴影之力，变的更加强大" /*[2]*/, 8 /*[3]*/, 100430 /*[4]*/],
		[36 /*[0]*/, 450170 /*[1]*/, "堕入阴影深渊的林精拥有更邪恶的力量" /*[2]*/, 9 /*[3]*/, 100440 /*[4]*/],
		[37 /*[0]*/, 460170 /*[1]*/, "魔笔将阴影之力灌注于笔墨之中，让人难以抵挡" /*[2]*/, 9 /*[3]*/, 100450 /*[4]*/],
		[38 /*[0]*/, 470170 /*[1]*/, "阴影使得永生燃魁首领拥有更坚硬的石肤，更炙热的能量" /*[2]*/, 9 /*[3]*/, 100460 /*[4]*/],
		[39 /*[0]*/, 480170 /*[1]*/, "附有阴影之力的毒液，不是常人可以抵抗的" /*[2]*/, 9 /*[3]*/, 100470 /*[4]*/],
		[40 /*[0]*/, 490170 /*[1]*/, "被阴影魔化的黑石，能够控制岩石进行毁灭性的攻击" /*[2]*/, 9 /*[3]*/, 100480 /*[4]*/],
		[41 /*[0]*/, 500170 /*[1]*/, "获得阴影之力的督军变得更加残暴" /*[2]*/, 10 /*[3]*/, 100490 /*[4]*/],
		[42 /*[0]*/, 510170 /*[1]*/, "修炼千年的竹筒精，拥有非常强大的阴影之力" /*[2]*/, 10 /*[3]*/, 100500 /*[4]*/],
		[43 /*[0]*/, 520170 /*[1]*/, "狂热的痴迷于财宝，导致被心魔影响，堕入深渊" /*[2]*/, 10 /*[3]*/, 100510 /*[4]*/],
		[44 /*[0]*/, 530170 /*[1]*/, "锦衣卫统领为了追求更强的力量，自甘堕落，吸收了阴影之力" /*[2]*/, 10 /*[3]*/, 100520 /*[4]*/],
		[45 /*[0]*/, 540170 /*[1]*/, "青冥剑枭和阴影之力完美融合，身上散溢出强大的邪恶气息" /*[2]*/, 10 /*[3]*/, 100530 /*[4]*/],
		[46 /*[0]*/, 550170 /*[1]*/, "你是否感到了阵阵妖风" /*[2]*/, 11 /*[3]*/, 100540 /*[4]*/],
		[47 /*[0]*/, 560170 /*[1]*/, "谁说玩火者自焚" /*[2]*/, 11 /*[3]*/, 100550 /*[4]*/],
		[48 /*[0]*/, 570170 /*[1]*/, "嗜血的奴隶" /*[2]*/, 11 /*[3]*/, 100560 /*[4]*/],
		[49 /*[0]*/, 580170 /*[1]*/, "吸收月之精华的狼妖" /*[2]*/, 11 /*[3]*/, 100570 /*[4]*/],
		[50 /*[0]*/, 590170 /*[1]*/, "似乎有些奇怪的东西" /*[2]*/, 11 /*[3]*/, 100580 /*[4]*/]
	],
};
