var equipment_recast_data = {
		/**
	 * 0 : id, tinyint, 主键ID
	 * 1 : level, int, 等级下限
	 * 2 : quality, tinyint, 品质
	 * 3 : fragment_num, smallint, 需要部位碎片数量
	 * 4 : blue_crystal_num, smallint, 需要蓝色结晶数量
	 * 5 : purple_crystal_num, smallint, 需要紫色结晶数量
	 * 6 : golden_crystal_num, smallint, 需要金色结晶数量
	 * 7 : orange_crystal_num, smallint, 需要橙色结晶数量
	 * 8 : consume_coin, bigint, 消耗的铜钱 
	 */

	Id : 0,
	Level : 1,
	Quality : 2,
	Fragment_num : 3,
	Blue_crystal_num : 4,
	Purple_crystal_num : 5,
	Golden_crystal_num : 6,
	Orange_crystal_num : 7,
	Consume_coin : 8,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[29 /*[0]*/, 1 /*[1]*/, 1 /*[2]*/, 2 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 1000 /*[8]*/],
		[36 /*[0]*/, 1 /*[1]*/, 2 /*[2]*/, 2 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 10000 /*[8]*/],
		[43 /*[0]*/, 1 /*[1]*/, 3 /*[2]*/, 8 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 40000 /*[8]*/],
		[50 /*[0]*/, 1 /*[1]*/, 4 /*[2]*/, 12 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 60000 /*[8]*/],
		[37 /*[0]*/, 10 /*[1]*/, 2 /*[2]*/, 4 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 20000 /*[8]*/],
		[51 /*[0]*/, 20 /*[1]*/, 4 /*[2]*/, 16 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 80000 /*[8]*/],
		[44 /*[0]*/, 20 /*[1]*/, 3 /*[2]*/, 12 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 60000 /*[8]*/],
		[30 /*[0]*/, 20 /*[1]*/, 1 /*[2]*/, 4 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 2000 /*[8]*/],
		[52 /*[0]*/, 40 /*[1]*/, 4 /*[2]*/, 20 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 100000 /*[8]*/],
		[45 /*[0]*/, 40 /*[1]*/, 3 /*[2]*/, 16 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 80000 /*[8]*/],
		[31 /*[0]*/, 40 /*[1]*/, 1 /*[2]*/, 8 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 4000 /*[8]*/],
		[38 /*[0]*/, 40 /*[1]*/, 2 /*[2]*/, 8 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 40000 /*[8]*/],
		[39 /*[0]*/, 60 /*[1]*/, 2 /*[2]*/, 12 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 60000 /*[8]*/],
		[53 /*[0]*/, 60 /*[1]*/, 4 /*[2]*/, 24 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 120000 /*[8]*/],
		[32 /*[0]*/, 60 /*[1]*/, 1 /*[2]*/, 12 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 6000 /*[8]*/],
		[46 /*[0]*/, 60 /*[1]*/, 3 /*[2]*/, 20 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 100000 /*[8]*/],
		[54 /*[0]*/, 80 /*[1]*/, 4 /*[2]*/, 28 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 140000 /*[8]*/],
		[33 /*[0]*/, 80 /*[1]*/, 1 /*[2]*/, 16 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 8000 /*[8]*/],
		[47 /*[0]*/, 80 /*[1]*/, 3 /*[2]*/, 24 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 120000 /*[8]*/],
		[40 /*[0]*/, 80 /*[1]*/, 2 /*[2]*/, 16 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 80000 /*[8]*/],
		[55 /*[0]*/, 100 /*[1]*/, 4 /*[2]*/, 32 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 160000 /*[8]*/],
		[48 /*[0]*/, 100 /*[1]*/, 3 /*[2]*/, 28 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 140000 /*[8]*/],
		[41 /*[0]*/, 100 /*[1]*/, 2 /*[2]*/, 20 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 100000 /*[8]*/],
		[34 /*[0]*/, 100 /*[1]*/, 1 /*[2]*/, 20 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 10000 /*[8]*/],
		[57 /*[0]*/, 120 /*[1]*/, 2 /*[2]*/, 24 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 120000 /*[8]*/],
		[58 /*[0]*/, 120 /*[1]*/, 3 /*[2]*/, 32 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 160000 /*[8]*/],
		[59 /*[0]*/, 140 /*[1]*/, 2 /*[2]*/, 28 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 140000 /*[8]*/],
		[60 /*[0]*/, 160 /*[1]*/, 2 /*[2]*/, 32 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 160000 /*[8]*/],
		[42 /*[0]*/, 500 /*[1]*/, 2 /*[2]*/, 32 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 160000 /*[8]*/],
		[35 /*[0]*/, 500 /*[1]*/, 1 /*[2]*/, 20 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 10000 /*[8]*/],
		[49 /*[0]*/, 500 /*[1]*/, 3 /*[2]*/, 28 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 140000 /*[8]*/],
		[56 /*[0]*/, 500 /*[1]*/, 4 /*[2]*/, 32 /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 160000 /*[8]*/]
	],
};
