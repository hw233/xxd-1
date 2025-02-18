var quest_start_award_data = {
		/**
	 * 0 : id, int, 主键
	 * 1 : name, varchar, 奖励名称
	 * 2 : stars, int, 所需星星数量
	 * 3 : ingot, int, 奖励元宝
	 * 4 : coin, bigint, 奖励铜钱
	 * 5 : heart, int, 奖励爱心
	 * 6 : item1, int, 奖励物品1
	 * 7 : item1_num, int, 奖励物品1数量
	 * 8 : item2, int, 奖励物品2
	 * 9 : item2_num, int, 奖励物品2数量
	 * 10 : item3, int, 奖励物品3
	 * 11 : item3_num, int, 奖励物品3数量
	 * 12 : item4, int, 奖励物品4
	 * 13 : item4_num, int, 奖励物品4数量
	 * 14 : item5, int, 奖励物品5
	 * 15 : item5_num, int, 奖励物品5数量 
	 */

	Id : 0,
	Name : 1,
	Stars : 2,
	Ingot : 3,
	Coin : 4,
	Heart : 5,
	Item1 : 6,
	Item1_num : 7,
	Item2 : 8,
	Item2_num : 9,
	Item3 : 10,
	Item3_num : 11,
	Item4 : 12,
	Item4_num : 13,
	Item5 : 14,
	Item5_num : 15,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, "初级青铜宝箱" /*[1]*/, 20 /*[2]*/, 0 /*[3]*/, 2000 /*[4]*/, 0 /*[5]*/, 236 /*[6]*/, 4 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[2 /*[0]*/, "中级青铜宝箱" /*[1]*/, 50 /*[2]*/, 0 /*[3]*/, 5000 /*[4]*/, 0 /*[5]*/, 237 /*[6]*/, 4 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[3 /*[0]*/, "高级青铜宝箱" /*[1]*/, 100 /*[2]*/, 0 /*[3]*/, 10000 /*[4]*/, 0 /*[5]*/, 238 /*[6]*/, 4 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[4 /*[0]*/, "初级白银宝箱" /*[1]*/, 120 /*[2]*/, 0 /*[3]*/, 12000 /*[4]*/, 0 /*[5]*/, 235 /*[6]*/, 8 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[5 /*[0]*/, "中级白银宝箱" /*[1]*/, 150 /*[2]*/, 0 /*[3]*/, 15000 /*[4]*/, 0 /*[5]*/, 236 /*[6]*/, 8 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[6 /*[0]*/, "高级白银宝箱" /*[1]*/, 200 /*[2]*/, 0 /*[3]*/, 20000 /*[4]*/, 0 /*[5]*/, 237 /*[6]*/, 8 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[7 /*[0]*/, "初级黄金宝箱" /*[1]*/, 220 /*[2]*/, 0 /*[3]*/, 22000 /*[4]*/, 0 /*[5]*/, 238 /*[6]*/, 8 /*[7]*/, 235 /*[8]*/, 8 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[8 /*[0]*/, "中级黄金宝箱" /*[1]*/, 250 /*[2]*/, 0 /*[3]*/, 25000 /*[4]*/, 0 /*[5]*/, 236 /*[6]*/, 8 /*[7]*/, 237 /*[8]*/, 8 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/],
		[9 /*[0]*/, "高级黄金宝箱" /*[1]*/, 300 /*[2]*/, 0 /*[3]*/, 30000 /*[4]*/, 0 /*[5]*/, 238 /*[6]*/, 8 /*[7]*/, 235 /*[8]*/, 8 /*[9]*/, 0 /*[10]*/, 0 /*[11]*/, 0 /*[12]*/, 0 /*[13]*/, 0 /*[14]*/, 0 /*[15]*/]
	],
};
