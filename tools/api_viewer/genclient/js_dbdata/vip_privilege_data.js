var vip_privilege_data = {
		/**
	 * 0 : id, int, ID
	 * 1 : name, varchar, 特权名称
	 * 2 : sign, varchar, 唯一标识
	 * 3 : tip, varchar, 特权描述
	 * 4 : order, int,  
	 */

	Id : 0,
	Name : 1,
	Sign : 2,
	Tip : 3,
	Order : 4,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, "爱心福利" /*[1]*/, "AiXinFuLi" /*[2]*/, "每天将通过邮件形式赠送爱心" /*[3]*/, 1 /*[4]*/],
		[8 /*[0]*/, "购买铜钱" /*[1]*/, "GouMaiTongQian" /*[2]*/, "每天给予额外的铜钱购买次数" /*[3]*/, 2 /*[4]*/],
		[15 /*[0]*/, "购买体力" /*[1]*/, "GouMaiTiLi" /*[2]*/, "每天给予额外的体力购买次数" /*[3]*/, 3 /*[4]*/],
		[23 /*[0]*/, "比武场特权" /*[1]*/, "BiWuChangTeQuan" /*[2]*/, "可使用元宝清除比武场冷却时间" /*[3]*/, 4 /*[4]*/],
		[27 /*[0]*/, "爱心抽奖" /*[1]*/, "AiXinChouJiang" /*[2]*/, "提高每天爱心抽奖次数上限" /*[3]*/, 6 /*[4]*/],
		[30 /*[0]*/, "瀛海集市" /*[1]*/, "YingHaiJiShi" /*[2]*/, "永久开启瀛海集市刷新功能" /*[3]*/, 7 /*[4]*/],
		[28 /*[0]*/, "批量兑换" /*[1]*/, "PiLiangDuiHuan" /*[2]*/, "开元通宝可使用批量兑换" /*[3]*/, 10 /*[4]*/],
		[29 /*[0]*/, "彩虹特权" /*[1]*/, "CaiHongTeQuan" /*[2]*/, "每天可购买更多彩虹关扫荡次数" /*[3]*/, 12 /*[4]*/],
		[37 /*[0]*/, "时装.武道" /*[1]*/, "ZhuanShuShiZhuang" /*[2]*/, "立刻获得专属永久时装”武道“（奖励唯一）" /*[3]*/, 18 /*[4]*/],
		[39 /*[0]*/, "比武场次数" /*[1]*/, "BiWuChangCiShu" /*[2]*/, "每日可购买更多比武场次数" /*[3]*/, 20 /*[4]*/],
		[41 /*[0]*/, "资源关卡扫荡" /*[1]*/, "ZiYuanGuanQiaSaoDang" /*[2]*/, "资源关卡扫荡" /*[3]*/, 21 /*[4]*/],
		[42 /*[0]*/, "云海特权" /*[1]*/, "YunHaiTeQuan" /*[2]*/, "云海御剑多次购买步数" /*[3]*/, 22 /*[4]*/],
		[43 /*[0]*/, "福地特权" /*[1]*/, "FuDiTeQuan" /*[2]*/, "每天可购买洞天福地额外次数" /*[3]*/, 23 /*[4]*/],
		[44 /*[0]*/, "绝望之地" /*[1]*/, "JueWangZhiDi" /*[2]*/, "绝望之地购买次数" /*[3]*/, 26 /*[4]*/],
		[40 /*[0]*/, "暂时不要删除" /*[1]*/, "HUNSHISHENGXING" /*[2]*/, "等程序来改" /*[3]*/, 99 /*[4]*/]
	],
};
