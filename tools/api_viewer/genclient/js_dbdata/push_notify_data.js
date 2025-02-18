var push_notify_data = {
		/**
	 * 0 : id, int, 公告模版ID
	 * 1 : sign, varchar, 唯一标识
	 * 2 : trigger_time, int, 触发时间一天内第几秒 [0,86400)
	 * 3 : content, varchar, 内容
	 * 4 : name, varchar, 推送通知名称 
	 */

	Id : 0,
	Sign : 1,
	Trigger_time : 2,
	Content : 3,
	Name : 4,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, "AfternoonPhysical" /*[1]*/, 43200 /*[2]*/, "大侠快来领取你的午市大餐吧~大侠快来领取体力吧~" /*[3]*/, "12点体力领取通知" /*[4]*/],
		[2 /*[0]*/, "NightPhysical" /*[1]*/, 64800 /*[2]*/, "我们已为你准备了香喷喷的晚餐，大侠快来领取体力吧~" /*[3]*/, "18点体力领取通知" /*[4]*/],
		[3 /*[0]*/, "SeaShop" /*[1]*/, 75600 /*[2]*/, "瀛海集市又进新货啦~大侠赶快来看一下吧！" /*[3]*/, "瀛海集市刷新通知" /*[4]*/],
		[4 /*[0]*/, "MaxPhysical" /*[1]*/, -1 /*[2]*/, "我们已经为大侠回复满体力了！赶快来继续探险吧！" /*[3]*/, "体力回复满通知" /*[4]*/],
		[5 /*[0]*/, "PrivateMessage" /*[1]*/, -1 /*[2]*/, "您有一位好友在游戏里给你发送了消息哦！快去看看他想悄悄告诉你什么！" /*[3]*/, "私聊消息通知" /*[4]*/],
		[6 /*[0]*/, "ArenaAttack" /*[1]*/, -1 /*[2]*/, "您在比武场遭到了挑战！快去看看是谁那么胆大包天！" /*[3]*/, "比武场被攻击通知" /*[4]*/]
	],
};
