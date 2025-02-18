var mail_data = {
		/**
	 * 0 : id, int, 邮件ID
	 * 1 : title, varchar, 标题
	 * 2 : parameters, varchar, 参数
	 * 3 : content, varchar, 内容
	 * 4 : expire_time, bigint, 邮件删除时机 0-默认过期删除 1-无附件已阅读自动删除 >1 指定时间删除
	 * 5 : priority, tinyint, 优先级
	 * 6 : max_level, smallint, 要求最高等级
	 * 7 : min_vip_level, smallint, 要求VIP最低等级
	 * 8 : max_vip_level, smallint, 要求VIP最等级
	 * 9 : min_level, smallint, 要求最低等级 
	 */

	Id : 0,
	Title : 1,
	Parameters : 2,
	Content : 3,
	Expire_time : 4,
	Priority : 5,
	Max_level : 6,
	Min_vip_level : 7,
	Max_vip_level : 8,
	Min_level : 9,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, "背包已满提示" /*[1]*/, "func,功能" /*[2]*/, "您的背包已满，系统已自动将{0}的物品暂存至附件，请及时点击领取" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[2 /*[0]*/, "爱心赠送邮件" /*[1]*/, "who,发送者" /*[2]*/, "您的好友{0}赠送您一颗爱心哦！请及时点击领取。" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[3 /*[0]*/, "测试邮件" /*[1]*/, "p1, 参数1; p2, 参数2" /*[2]*/, "我{0}只是一封测试邮件{1}，虽然偶只是测试用的，但四，你八可以八理我，if你不点我我that会伤心的。so !选我！选我！选我！" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[4 /*[0]*/, "多人关卡战斗奖励" /*[1]*/, "name,关卡名称" /*[2]*/, "您在参与的多人关卡{0}中取得了胜利，附件里是您获得的奖励。" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[6 /*[0]*/, "魂侍背包已满提示" /*[1]*/, "func,功能" /*[2]*/, "您的魂侍背包已满，系统已自动将您刚抽取到的{0}个魂侍暂存至附件，请及时点击领取。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[7 /*[0]*/, "剑心背包已满提示" /*[1]*/, "func,功能" /*[2]*/, "您的剑心背包已满，系统已自动将您刚抽取到的{0}个剑心暂存至附件，请及时点击领取。" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[8 /*[0]*/, "充值成功" /*[1]*/, "time1,时间; num,充值元宝数量" /*[2]*/, "恭喜您在{0}成功充值{1}元宝，仙侠道团队感谢您对我们游戏的支持。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[9 /*[0]*/, "购买道具成功提示" /*[1]*/, "source,来源;item_name,道具名称;func,功能;" /*[2]*/, "尊敬的大侠，恭喜您刚刚从{0}得到了{1}，此道具可在{2}功能开放后在此系统背包中查看。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[10 /*[0]*/, "神龙宝箱获得提示" /*[1]*/, "item_name,道具名称;func,功能;" /*[2]*/, "尊敬的大侠，恭喜您刚刚得到了{0}，此道具可在{1}功能开放后在此系统背包中查看。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[11 /*[0]*/, "邀请好友奖励" /*[1]*/, "friend_num,人数;item_num,数字;item_name,道具" /*[2]*/, "又有小伙伴加入我们的大家庭啦～恭喜大侠的好友数已达到{0}人，我们很愉快的赠送给您{1}个{2}，邀请更多好友加入仙侠道，有更多精彩好礼等您来拿。" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[12 /*[0]*/, "感谢参与封测" /*[1]*/, "" /*[2]*/, "这是《仙侠道》首次与广大仙友的亲密接触，欢迎大家在体验过程中提出各种宝贵的意见和建议。\n官方QQ交流群：397324414" /*[3]*/, 0 /*[4]*/, 1 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[13 /*[0]*/, "比武场宝箱领取提醒" /*[1]*/, "nun,排名" /*[2]*/, "尊敬的大侠～您在比武场的精彩表现万众瞩目～截止昨日24点，您的比武场排名为{0}，快去比武场领取您的比武场宝箱吧～" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[14 /*[0]*/, "仙尊每日爱心" /*[1]*/, "" /*[2]*/, "您是一位让人爱戴的侠客！" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[15 /*[0]*/, "升级活动（废弃）" /*[1]*/, "" /*[2]*/, "活动时间：内测期间\n活动内容：玩家等级达到相应条件，就可领取对应奖励\n活动奖励：\n5级—30级   每提升5级即可获得“5个铜钱袋”\n35级—60级  每提升5级即可获得“10个铜钱袋”\n（奖励也将通过邮件形式发放，请注意查收）" /*[3]*/, 1 /*[4]*/, 1 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[17 /*[0]*/, "升级活动奖励（废弃）" /*[1]*/, "" /*[2]*/, "升级活动奖励，请注意查收" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[18 /*[0]*/, "仙尊签到奖励" /*[1]*/, "" /*[2]*/, "尊敬的仙尊玩家，以下是本次仙尊双倍奖励内容，请注意查收。" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[19 /*[0]*/, "战力活动" /*[1]*/, "" /*[2]*/, "活动时间：内测期间\n活动内容：玩家队伍战力达到相应条件，就可领取对应奖励\n活动奖励：\n总战力5000    奖励58元宝\n总战力10000  奖励68元宝\n总战力20000  奖励88元宝\n总战力30000  奖励128元宝\n总战力40000  奖励188元宝\n总战力50000  奖励248元宝\n总战力60000  奖励388元宝\n（奖励也将通过邮件形式发放，请注意查收）" /*[3]*/, 0 /*[4]*/, 1 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[20 /*[0]*/, "战力活动奖励" /*[1]*/, "" /*[2]*/, "战力活动奖励，请注意查收" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[22 /*[0]*/, "仙尊特权奖励" /*[1]*/, "vip_num,vip等级" /*[2]*/, "恭喜您提升到仙尊{0}级，请注意查收奖励内容" /*[3]*/, 1 /*[4]*/, 1 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[23 /*[0]*/, "道具获得提示" /*[1]*/, "item_name,道具名称;func,功能;" /*[2]*/, "尊敬的大侠，恭喜您刚刚得到了{0}，此道具可在{1}功能开放后在此系统背包中查看。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[24 /*[0]*/, "七日新手礼活动（废弃）" /*[1]*/, "" /*[2]*/, "感谢您对仙侠道的支持，以下是今日登入奖励！" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[25 /*[0]*/, "打坐小提醒" /*[1]*/, "" /*[2]*/, "尊敬的大侠，通过不断的努力，您已经能够进行打坐啦！为了能够更快提升实力拯救大地，当您离线10分钟后将会自动进入打坐状态哦~！" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[26 /*[0]*/, "注册好礼" /*[1]*/, "" /*[2]*/, "欢迎大侠进入仙侠道的世界！在此送上我们的一点小心意！请注意查收哦！请大侠愉快的玩耍吧！" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[28 /*[0]*/, "侠客见面礼" /*[1]*/, "" /*[2]*/, "欢迎大侠进入仙侠道！在此送上我们的小小心意！大侠注意查收哦！" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[29 /*[0]*/, "首充豪华礼" /*[1]*/, "" /*[2]*/, "恭喜大侠获得首充豪华礼，请注意查收附件" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[30 /*[0]*/, "胧月参上" /*[1]*/, "" /*[2]*/, "胧月很高兴能成为您的伙伴与您共闯仙侠道，在此为您奉上胧月的专属武器及魂侍，赶快装备起来让胧月变得更强吧！" /*[3]*/, 1 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[31 /*[0]*/, "新春红包活动奖励" /*[1]*/, "" /*[2]*/, "尊敬的大侠，感谢您一直以来对仙侠道的支持，新春之际给您送上一个大大的红包~快打开看看吧~" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[32 /*[0]*/, "会员独享新手礼包" /*[1]*/, "" /*[2]*/, "尊敬的会员玩家，在次奉上会员独享新手礼包，请注意查收。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[33 /*[0]*/, "超级会员尊贵新手礼包" /*[1]*/, "" /*[2]*/, "尊贵的超级会员玩家，在此为您奉上超级会员尊贵新手礼包，愿您畅游仙侠道的世界。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[34 /*[0]*/, "会员开通/续费礼包" /*[1]*/, "" /*[2]*/, "尊敬的玩家，感谢您开通/续费QQ会员，在此奉上专属礼包，请注意查收。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[35 /*[0]*/, "超级会员开通/续费礼包" /*[1]*/, "" /*[2]*/, "尊敬的玩家，感谢您开通/续费QQ超级会员，在此奉上专属礼包，请注意查收。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[36 /*[0]*/, "阵印背包已满提示" /*[1]*/, "num,数量" /*[2]*/, "您的阵印背包已满，系统已自动将您刚抽取到的{0}个阵印暂存至附件，请及时点击领取。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[37 /*[0]*/, "帮派邮件" /*[1]*/, "name,帮派名;num,帮派人数;coins,奖励铜钱" /*[2]*/, "尊敬的帮主，您管理的{0}帮派成员已达{1}人，获得每日帮派工资{2}铜钱！" /*[3]*/, 14 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[38 /*[0]*/, "帮派邮件" /*[1]*/, "name,帮派名;num,帮派人数;coins,奖励铜钱" /*[2]*/, "尊敬的副帮主，您管理的{0}帮派成员已达{1}人，获得每日帮派工资{2}铜钱" /*[3]*/, 14 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[39 /*[0]*/, "帮派邮件" /*[1]*/, "name,帮派名" /*[2]*/, "对不起，您被踢出了{0}帮派。！" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[40 /*[0]*/, "帮派邮件" /*[1]*/, "" /*[2]*/, "恭喜您，您被提升为副帮主，每日可获得帮派工资（帮众人数*100）。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[41 /*[0]*/, "帮派邮件" /*[1]*/, "" /*[2]*/, "对不起，您的副帮主职务已被撤除" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[42 /*[0]*/, "帮派邮件" /*[1]*/, "name,新任帮主" /*[2]*/, "对不起，由于您长时间没有上线，{0}弹劾了您，成为了帮派的新帮主。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[43 /*[0]*/, "帮派邮件" /*[1]*/, "name,老帮主" /*[2]*/, "经过慎重考虑，{0}决定退位让贤，将帮主之位让给您，恭喜您成为新帮主" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[44 /*[0]*/, "帮派邮件" /*[1]*/, "name,帮派名" /*[2]*/, "很遗憾，您的帮派{0}已解散" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[45 /*[0]*/, "上香祈福" /*[1]*/, "num,铜钱数量" /*[2]*/, "今日帮派祈福灯已点满，您获得{0}铜钱奖励" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[46 /*[0]*/, "帮派邮件" /*[1]*/, "" /*[2]*/, "您持有的金券、银券已中止兑换，现将您的投资原价退还。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[47 /*[0]*/, "帮派邮件" /*[1]*/, "name,帮派名" /*[2]*/, "您的帮派申请已被通过，恭喜您加入{0}" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[48 /*[0]*/, "豪华等级礼包" /*[1]*/, "" /*[2]*/, "亲爱的大侠，恭喜您已经达到20级。为感谢您得付出，在此我们为您送上一份豪华等级礼包，请注意查收。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[49 /*[0]*/, "Boss讨伐奖励" /*[1]*/, "boss_name,Boss名称;hurt,伤害;exp,经验数量;coins,铜钱数量;fame,声望数量" /*[2]*/, "你在本次讨伐{0}作战中，累计造成{1}点伤害，获得{2}点经验，{3}点铜钱，{4}点声望" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[50 /*[0]*/, "Boss讨伐精英奖励" /*[1]*/, "boss_name,Boss名称;rank,伤害排名;hurt,伤害;exp,经验数量;coins,铜钱数量;fame,声望数量" /*[2]*/, "你在本次讨伐{0}作战中，排名第{1}，累计造成{2}点伤害，获得{3}点经验，{4}点铜钱，{5}点声望，额外获得一个希望宝箱" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[51 /*[0]*/, "讨伐胜利" /*[1]*/, "camp_name,敌人军团名称;point,讨伐点数量;hope,希望之光数量" /*[2]*/, "你在此次对{0}的讨伐中表现英勇，累计获得{1}讨伐点，为击退敌人做出了杰出的贡献，特此奖励{2}希望之光，英雄请再接再厉！" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[52 /*[0]*/, "帮派宝箱福利" /*[1]*/, "" /*[2]*/, "大家对帮派的贡献日月可鉴，特此发放帮派宝箱福利，请大家再接再厉" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[53 /*[0]*/, "帮派军粮福利" /*[1]*/, "" /*[2]*/, "大家对帮派的贡献日月可鉴，特此发放帮派军粮福利，请大家再接再厉" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[54 /*[0]*/, "您在比武场被挑战" /*[1]*/, "name,挑战者" /*[2]*/, "{0}挑战了你，你获得了胜利，排名未发生变" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[55 /*[0]*/, "您在比武场被挑战" /*[1]*/, "name,挑战者;rank,排名;" /*[2]*/, "{0}挑战了你，你失败了，排名下降至{1}" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[56 /*[0]*/, "兔帮踢馆帮派伤害排行奖励" /*[1]*/, "clique_name,帮派名;rank,排名;item,物品名" /*[2]*/, "你所在的帮派{0}在此次对刀疤兔的讨伐中表现英勇，排名第{1}，获得一个{2}" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[59 /*[0]*/, "兔帮踢馆个人伤害奖励" /*[1]*/, "hurt,伤害;exp,经验;coins,铜钱;contri,帮贡" /*[2]*/, "你在此次对刀疤兔的讨伐中表现英勇，累计造成{0}点伤害，特此奖励{1}经验、{2}铜钱、{3}帮贡，英雄请再接再厉!" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[60 /*[0]*/, "兔帮踢馆个人伤害排行奖励" /*[1]*/, "rank,排名;item,物品名" /*[2]*/, "你在此次对刀疤兔的讨伐中表现英勇，排名第{0}，获得一个{1}" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[61 /*[0]*/, "帮派战报名结果" /*[1]*/, "battle_clique_name,帮派名" /*[2]*/, "您所在的帮派将在本周日19:30~20:00与{0}帮进行帮派战，大侠务必记得上线参与。" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[62 /*[0]*/, "帮派战报名失败" /*[1]*/, "" /*[2]*/, "你所在的帮派总战力太低，报名匹配失败！" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[63 /*[0]*/, "帮派战结果" /*[1]*/, "battle_clique_name,帮派名;point1,我方得分;point2,对方得分" /*[2]*/, "您所在的帮派将在与{0}帮的帮战中以{1}比{2}获胜，大侠请收下这个荣耀宝箱" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/],
		[64 /*[0]*/, "帮派战结果" /*[1]*/, "battle_clique_name,帮派名;point1,我方得分;point2,对方得分" /*[2]*/, "您所在的帮派将在与{0}帮的帮战中以{1}比{2}惜败，大侠请不要气馁" /*[3]*/, 0 /*[4]*/, 0 /*[5]*/, 0 /*[6]*/, 0 /*[7]*/, 0 /*[8]*/, 0 /*[9]*/]
	],
};
