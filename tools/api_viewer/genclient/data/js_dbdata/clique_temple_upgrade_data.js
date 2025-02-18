var clique_temple_upgrade_data = {
		/**
	 * 0 : id, int, 标识ID
	 * 1 : upgrade_fee, int, 升级费用（铜钱）
	 * 2 : level, smallint, 宗祠等级
	 * 3 : desc, text, 对应等级描述
	 * 4 : cur_temple_desc, text, 当前武功描述
	 * 5 : next_temple_desc, text, 下一等级武功描述 
	 */

	Id : 0,
	Upgrade_fee : 1,
	Level : 2,
	Desc : 3,
	Cur_temple_desc : 4,
	Next_temple_desc : 5,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[50 /*[0]*/, 300000 /*[1]*/, 0 /*[2]*/, "建设后开启帮派上香祈福\n升级建筑可以提升上香收益" /*[3]*/, "无" /*[4]*/, "开启上香功能" /*[5]*/],
		[51 /*[0]*/, 600000 /*[1]*/, 1 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡正常收益" /*[3]*/, "声望和帮贡正常收益" /*[4]*/, "声望和帮贡收益增加10%" /*[5]*/],
		[52 /*[0]*/, 800000 /*[1]*/, 2 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加10%" /*[3]*/, "声望和帮贡收益增加10%" /*[4]*/, "声望和帮贡收益增加15%" /*[5]*/],
		[53 /*[0]*/, 1000000 /*[1]*/, 3 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加15%" /*[3]*/, "声望和帮贡收益增加15%" /*[4]*/, "声望和帮贡收益增加20%" /*[5]*/],
		[54 /*[0]*/, 1200000 /*[1]*/, 4 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加20%" /*[3]*/, "声望和帮贡收益增加20%" /*[4]*/, "声望和帮贡收益增加25%" /*[5]*/],
		[55 /*[0]*/, 1600000 /*[1]*/, 5 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加25%" /*[3]*/, "声望和帮贡收益增加25%" /*[4]*/, "声望和帮贡收益增加30%" /*[5]*/],
		[56 /*[0]*/, 2000000 /*[1]*/, 6 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加30%" /*[3]*/, "声望和帮贡收益增加30%" /*[4]*/, "声望和帮贡收益增加35%" /*[5]*/],
		[57 /*[0]*/, 2400000 /*[1]*/, 7 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加35%" /*[3]*/, "声望和帮贡收益增加35%" /*[4]*/, "声望和帮贡收益增加40%" /*[5]*/],
		[58 /*[0]*/, 2800000 /*[1]*/, 8 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加40%" /*[3]*/, "声望和帮贡收益增加40%" /*[4]*/, "声望和帮贡收益增加45%" /*[5]*/],
		[59 /*[0]*/, 3200000 /*[1]*/, 9 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加45%" /*[3]*/, "声望和帮贡收益增加45%" /*[4]*/, "声望和帮贡收益增加50%" /*[5]*/],
		[60 /*[0]*/, 6000000 /*[1]*/, 10 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加50%" /*[3]*/, "声望和帮贡收益增加50%" /*[4]*/, "声望和帮贡收益增加55%" /*[5]*/],
		[61 /*[0]*/, 8000000 /*[1]*/, 11 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加55%" /*[3]*/, "声望和帮贡收益增加55%" /*[4]*/, "声望和帮贡收益增加60%" /*[5]*/],
		[62 /*[0]*/, 0 /*[1]*/, 12 /*[2]*/, "供奉帮派神明的祠堂，可供帮众上香\n当前上香声望和帮贡收益增加60%" /*[3]*/, "声望和帮贡收益增加60%" /*[4]*/, "无" /*[5]*/]
	],
};
