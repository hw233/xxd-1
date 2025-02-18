var mission_data = {
		/**
	 * 0 : id, smallint, 区域ID
	 * 1 : town_id, smallint, 城镇ID
	 * 2 : keys, int, 开启钥匙数
	 * 3 : name, varchar, 区域名称
	 * 4 : sign, varchar, 资源标识
	 * 5 : order, tinyint, 区域开启顺序 
	 */

	Id : 0,
	Town_id : 1,
	Keys : 2,
	Name : 3,
	Sign : 4,
	Order : 5,

	Each: function(cb) {
		for(var i = 0; i < this._list.length; i++) {
			cb(this._list[i]);
		}
	},

	_list: [
		[1 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/, "青竹林" /*[3]*/, "QingZhuLin" /*[4]*/, 1 /*[5]*/],
		[2 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/, "黑夜森林" /*[3]*/, "HeiYeSenLin" /*[4]*/, 2 /*[5]*/],
		[3 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/, "莲花峰" /*[3]*/, "LianHuaFeng" /*[4]*/, 3 /*[5]*/],
		[4 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/, "熔岩火山" /*[3]*/, "RongYanHuoShan" /*[4]*/, 4 /*[5]*/],
		[5 /*[0]*/, 1 /*[1]*/, 0 /*[2]*/, "剑灵密室" /*[3]*/, "JianLingMiShi" /*[4]*/, 5 /*[5]*/],
		[6 /*[0]*/, 3 /*[1]*/, 999 /*[2]*/, "测试区域" /*[3]*/, "QingZhuLin" /*[4]*/, 126 /*[5]*/],
		[7 /*[0]*/, 2 /*[1]*/, 0 /*[2]*/, "血雾岭" /*[3]*/, "XueWuLing" /*[4]*/, 6 /*[5]*/],
		[8 /*[0]*/, 2 /*[1]*/, 0 /*[2]*/, "青丘山" /*[3]*/, "QingQiuShan" /*[4]*/, 7 /*[5]*/],
		[9 /*[0]*/, 2 /*[1]*/, 0 /*[2]*/, "神木林" /*[3]*/, "ShenMuLin" /*[4]*/, 8 /*[5]*/],
		[10 /*[0]*/, 2 /*[1]*/, 0 /*[2]*/, "泼墨斋" /*[3]*/, "PoMoZhai" /*[4]*/, 9 /*[5]*/],
		[11 /*[0]*/, 2 /*[1]*/, 0 /*[2]*/, "虚天殿" /*[3]*/, "XuTianDian" /*[4]*/, 10 /*[5]*/],
		[12 /*[0]*/, 4 /*[1]*/, 0 /*[2]*/, "桃花林" /*[3]*/, "TaoHuaLin" /*[4]*/, 11 /*[5]*/],
		[13 /*[0]*/, 4 /*[1]*/, 0 /*[2]*/, "问剑崖" /*[3]*/, "WenJianYa" /*[4]*/, 12 /*[5]*/],
		[14 /*[0]*/, 4 /*[1]*/, 0 /*[2]*/, "昆墟" /*[3]*/, "KunXu" /*[4]*/, 13 /*[5]*/],
		[15 /*[0]*/, 4 /*[1]*/, 0 /*[2]*/, "剑冢" /*[3]*/, "JianZhong" /*[4]*/, 14 /*[5]*/],
		[16 /*[0]*/, 4 /*[1]*/, 0 /*[2]*/, "帝皇陵" /*[3]*/, "DiHuangLing" /*[4]*/, 15 /*[5]*/],
		[17 /*[0]*/, 5 /*[1]*/, 0 /*[2]*/, "云梦山" /*[3]*/, "YunMengShan" /*[4]*/, 16 /*[5]*/],
		[18 /*[0]*/, 5 /*[1]*/, 0 /*[2]*/, "沙漠绿洲" /*[3]*/, "ShaMoLvZhou" /*[4]*/, 17 /*[5]*/],
		[19 /*[0]*/, 5 /*[1]*/, 0 /*[2]*/, "逆水寒潭" /*[3]*/, "NiShuiHanTan" /*[4]*/, 18 /*[5]*/],
		[20 /*[0]*/, 5 /*[1]*/, 0 /*[2]*/, "幻境森林" /*[3]*/, "HuanJingSenLin" /*[4]*/, 19 /*[5]*/],
		[21 /*[0]*/, 5 /*[1]*/, 0 /*[2]*/, "失落神庙" /*[3]*/, "ShiLuoShenMiao" /*[4]*/, 20 /*[5]*/],
		[22 /*[0]*/, 3 /*[1]*/, 999 /*[2]*/, "剧情用地图勿删" /*[3]*/, "QingZhuLin" /*[4]*/, 127 /*[5]*/],
		[23 /*[0]*/, 6 /*[1]*/, 0 /*[2]*/, "常乐坊" /*[3]*/, "ChangLeFang" /*[4]*/, 21 /*[5]*/],
		[24 /*[0]*/, 6 /*[1]*/, 0 /*[2]*/, "江户沙滩" /*[3]*/, "JiangHuShaTan" /*[4]*/, 22 /*[5]*/],
		[25 /*[0]*/, 6 /*[1]*/, 0 /*[2]*/, "江户城" /*[3]*/, "JiangHuChen" /*[4]*/, 23 /*[5]*/],
		[26 /*[0]*/, 6 /*[1]*/, 0 /*[2]*/, "地下龙城" /*[3]*/, "DiXiaLongChen" /*[4]*/, 24 /*[5]*/],
		[27 /*[0]*/, 6 /*[1]*/, 0 /*[2]*/, "地底火山" /*[3]*/, "DiDiHuoShan" /*[4]*/, 25 /*[5]*/],
		[28 /*[0]*/, 7 /*[1]*/, 0 /*[2]*/, "唐家堡" /*[3]*/, "TangJiaBao" /*[4]*/, 26 /*[5]*/],
		[29 /*[0]*/, 7 /*[1]*/, 0 /*[2]*/, "刀殿" /*[3]*/, "DaoDian" /*[4]*/, 27 /*[5]*/],
		[30 /*[0]*/, 7 /*[1]*/, 0 /*[2]*/, "剑宗" /*[3]*/, "JianZong" /*[4]*/, 28 /*[5]*/],
		[31 /*[0]*/, 7 /*[1]*/, 0 /*[2]*/, "玄音寺" /*[3]*/, "XuanYinSi" /*[4]*/, 29 /*[5]*/],
		[32 /*[0]*/, 7 /*[1]*/, 0 /*[2]*/, "五行宫" /*[3]*/, "WuXingGong" /*[4]*/, 30 /*[5]*/],
		[33 /*[0]*/, 8 /*[1]*/, 0 /*[2]*/, "蛮族森林" /*[3]*/, "ManZuSenLin" /*[4]*/, 31 /*[5]*/],
		[34 /*[0]*/, 8 /*[1]*/, 0 /*[2]*/, "哀嚎石崖" /*[3]*/, "AiHaoShiYa" /*[4]*/, 32 /*[5]*/],
		[35 /*[0]*/, 8 /*[1]*/, 0 /*[2]*/, "寂静林" /*[3]*/, "JiJingLin" /*[4]*/, 33 /*[5]*/],
		[36 /*[0]*/, 8 /*[1]*/, 0 /*[2]*/, "八卦山道" /*[3]*/, "BaGuaShanDao" /*[4]*/, 34 /*[5]*/],
		[37 /*[0]*/, 8 /*[1]*/, 0 /*[2]*/, "噩梦之地" /*[3]*/, "EMengZhiDi" /*[4]*/, 35 /*[5]*/],
		[38 /*[0]*/, 9 /*[1]*/, 0 /*[2]*/, "竹林幻境" /*[3]*/, "ZhuLinHuanJing" /*[4]*/, 36 /*[5]*/],
		[39 /*[0]*/, 9 /*[1]*/, 0 /*[2]*/, "嵎夷阵眼" /*[3]*/, "YuYiZhenYan" /*[4]*/, 37 /*[5]*/],
		[40 /*[0]*/, 9 /*[1]*/, 0 /*[2]*/, "南交阵眼" /*[3]*/, "NanJiaoZhenYan" /*[4]*/, 38 /*[5]*/],
		[41 /*[0]*/, 9 /*[1]*/, 0 /*[2]*/, "昧谷阵眼" /*[3]*/, "MeiGuZhenYan" /*[4]*/, 39 /*[5]*/],
		[42 /*[0]*/, 9 /*[1]*/, 0 /*[2]*/, "幽都阵眼" /*[3]*/, "YouDuZhenYan" /*[4]*/, 40 /*[5]*/],
		[43 /*[0]*/, 10 /*[1]*/, 0 /*[2]*/, "重回蛮荒" /*[3]*/, "ChongHuiManHuang" /*[4]*/, 41 /*[5]*/],
		[44 /*[0]*/, 10 /*[1]*/, 0 /*[2]*/, "城外竹林" /*[3]*/, "ChengWaiZhuLin" /*[4]*/, 42 /*[5]*/],
		[45 /*[0]*/, 10 /*[1]*/, 0 /*[2]*/, "梨园义地" /*[3]*/, "LiYuanYiDi" /*[4]*/, 43 /*[5]*/],
		[46 /*[0]*/, 10 /*[1]*/, 0 /*[2]*/, "皇城城墙" /*[3]*/, "HuangChengChengQiang" /*[4]*/, 44 /*[5]*/],
		[47 /*[0]*/, 10 /*[1]*/, 0 /*[2]*/, "极暗之地" /*[3]*/, "JiAnZhiDi" /*[4]*/, 45 /*[5]*/]
	],
};
