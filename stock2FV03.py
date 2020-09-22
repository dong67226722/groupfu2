econding = "utf-8"
import os
import time
import math
import codecs
import copy
import hwxsGn

stockPhs = []
#定义主界面显示函数
def printMenu():
	print("="*128)
	print("      群福塑胶制品有限公司仓库看板系统v01")
	print("                                               ")
	print("1.仓库入库功能")
	print("2.修改仓库存货功能")
	print("3.储位查询及修改储位功能")
	print("4.删除存货功能")
	print("5.展示仓库存货品号信息")
	print("6.存档功能")
	print("7.品号查询存货功能")
	print("8.出库管理功能")
	print("9.库龄查询及制令追溯查询功能")
	print("0.退出仓库看板系统")
	print("                                               ")
	print("="*128)
#扫描二维码拆分返回资料函数，可优化加入入库功能使用
def splitQrcd():
	a = input("请扫描货物二维码：")
	newName = a[16:27]
	b = a.rfind("-")
	newPcb = int(a[28:b])
	return {'newName',newName,'newPcb',newPcb}
	# print(newName,"包装是：",newPcb)
#出库信息拆分函数，待加入出货函数使用
def stockOutcomde():
	a = int(input("请选择出库方式, 1 是扫描输入出货资料，2 键盘输入出货资料:"))
	if a == 1:
		newComde = input("请扫描出货资料条形码：")
		b = newComde.find("-")
		c = newComde.rfind("-")
		orderNum = newComde[0:b]
		stk = newComde[(b+1):(b+11)]
		ouTsums = int(newComde[(c+1):])
		print("此批出库资讯是：", "品号：", stk, "数量：", ouTsums, "订单是：", orderNum)
	elif a == 2:
		orderNum = input("请输入订单号码：")
		stk = input("请输入要出库的品号：")
		ouTsums = int(input("请输入出库数量："))
		print("此批出库资讯是：", "品号：", stk, "数量：", ouTsums, "订单是：", orderNum)



#定义新增品号函数即是入库函数
def newInfo():
	a = int(input("请选择输入方式, 1 是新QRcode全扫描输入，2 是扫旧QRcode与键盘混合输入:"))
	if a == 1:
		# splitQrcd()
		newQr = input("请扫描货物二维码：")
		newName = newQr[16:27]
		b = newQr.rfind("-")
		newPcb = newQr[28:b]
		newCoton = int(input("请输入入库箱数："))
		newSite = input("请输入存货位置信息：")
		newNum = int(newPcb)* newCoton
		print("此批入库资讯是：","品号：",newName,"数量：",newNum,"位置是：",newSite)
	elif a == 2:
		newQr = input("请扫描货物二维码：")
		newName = input("请输入新入的品号信息：")
		newNum = input("请输入入库数信息：")
		newCoton = int(input("请输入入库箱数："))
		newSite = input("请输入存货位置信息：")
		print("此批入库资讯是：","品号：",newName,"数量：",newNum,"位置是：",newSite)

	timea = time.time()
	timeArray = time.localtime(timea)

	stockPh = {}
	
	stockPh['stockID'] = newName
	stockPh['Site'] = newSite
	stockPh['Num.'] = newNum
	stockPh['coton'] = newCoton
	stockPh['inTime'] = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
	stockPh['Qrcd'] = newQr
	stockPhs.append(stockPh)

#修改存货功能
def modifInfo():
	a = int(input("请选择修改方式, 1 是新QRcode全扫描输入，2 是键盘输入修改:"))
	if a == 1:
		# stoId = int(input("请输入需要修改存货序号："))
		newQr = input("请扫描货物二维码：")
		for tem in stockPhs:
			if tem['Qrcd'] == newQr:
				temNum = stockPhs.index(tem)
		newName = newQr[16:27]
		b = newQr.rfind("-")
		newPcb = newQr[28:b]
		newCoton = int(input("请输入入库箱数："))
		newSite = input("请输入存货位置信息：")
		newNum = int(newPcb) * newCoton
		print("此批修改入库资讯是：", "品号：", newName, "数量：", newNum, "位置是：", newSite)

	elif a == 2:
		# stoId = int(input("请输入需要修改存货序号："))
		newQr = input("请扫描货物二维码：")
		for tem in stockPhs:
			if tem['Qrcd'] == newQr:
				temNum = stockPhs.index(tem)
		newName = input("请输入新入的品号信息：")
		newSite = input("请输入存货位置信息：")
		newCoton = int(input("请输入入库箱数："))
		newNum = int(input("请输入入库数量："))
		newTime = input("请输入入库日期信息，格式%Y-%m-%d %H:%M:%S ：")
		stockPhs[temNum]['inTime'] = newTime

	stockPhs[temNum]['Qrcd'] = newQr
	stockPhs[temNum]['stockID'] = newName
	stockPhs[temNum]['Site'] = newSite
	stockPhs[temNum]['Num.'] = newNum
	stockPhs[temNum]['coton'] = newCoton

#位置查询存货功能
def siteCx():
	cx = int(input("请输入要执行的功能：1 查询储位存货信息，2 按二维码修改存货储位！3 按地址码修改存货储位！"))
	if cx == 1:
		a = input("请输入查询存货位置：")
		print("序号----品号-----------位置------数量-----箱数-------入库时间----------------'Qrcd'")
		j = 1
		for tem in stockPhs:
			if tem['Site'] == a:
				print("%-4d    %-12s    %-6s   %-6s   %-6s  %-22s   %-10s"%(j,tem['stockID'],tem['Site'],tem['Num.'],tem['coton'],tem['inTime'],tem['Qrcd']))
				j+=1
	elif cx == 2:
		b = input("请扫描存货二维码：")
		for tem in stockPhs:
			if tem['Qrcd'] == b:
				temNum = stockPhs.index(tem)
				xgSite = input("请输入新的储位信息：")
				stockPhs[int(temNum)]['Site'] = xgSite
				print("调整储位到",xgSite,"完成！")
			else:
				pass
	elif cx == 3:
		b = input("请扫描旧存货地址码：")
		xgSite = input("请输入新的储位信息：")
		siteNum = 0
		for tem in stockPhs:
			if tem['Site'] == str(b):
				temNum = stockPhs.index(tem)
				stockPhs[int(temNum)]['Site'] = xgSite
				siteNum+=1
			else:
				pass
		if siteNum>0:
			print("调整储位",b,"的", siteNum, "笔存货到", xgSite, "完成！")
		else:
			print("旧存货信息没有！请重新选择功能")
		# xgSite = input("请输入新的储位信息：")
		# stockPhs[int(temNum)]['Site'] = xgSite

#出库功能，自动记录订单出库追溯信息，所有订单出库资料全部存档可用于按制令追溯
def ouTstock():

	inp = int(input("请选择出库方式, 1 是扫描输入出货资料，2 键盘输入出货资料:"))
	if inp == 1:
		newComde = input("请扫描出货资料条形码：")
		b = newComde.find("-")
		c = newComde.rfind("-")
		orderNum = newComde[0:b]
		stk = newComde[(b + 1):(b + 12)]
		ouTsums = int(newComde[(c + 1):])
		print("此批出库资讯是：", "品号：", stk, "数量：", ouTsums, "订单是：", orderNum)
	elif inp == 2:
		orderNum = input("请输入订单号码：")
		stk = input("请输入要出库的品号：")
		ouTsums = int(input("请输入出库数量："))
		print("此批出库资讯是：", "品号：", stk, "数量：", ouTsums, "订单是：", orderNum)

	global stockPhs
	global a
	a = 0
	ouTstocks = []
	outxs = 0
	# sums = copy.deepcopy(ouTsums)
	# stockPhs = [x for x in stockPhs if x['stockID'] != stk]

	for tem in stockPhs:
		if tem['stockID'] == stk and tem not in ouTstocks:
			ouTstocks.append(tem)
			outxs = outxs + int(tem['Num.'])

	if outxs < ouTsums:
		print("=" * 80)
		print("老板！库存不足了，需要出库",ouTsums,"实际库存:",outxs,"赶紧生产！")
		pass
	else:
		sums = copy.deepcopy(ouTsums)
		stockPhs =[x for x in stockPhs if x['stockID'] != stk ]


		ouT1 = sorted(ouTstocks, key=lambda k_v: k_v['inTime'])
		outL1 = copy.deepcopy(ouT1)

		out1Nums = []
		j = 0
		while sums > 0:
		# for l,m in enumerate(ouT1):
			if int(ouT1[j]['Num.']) <= int(sums):
				sums = sums - int(ouT1[j]['Num.'])
				out1Nums.append(j)
				j += 1
			elif int(ouT1[j]['Num.']) >int(sums):
				a = int(ouT1[j]['Num.']) -int(sums)
				# ouT1[j]['Num.'] = str(a)
				outL1[j]['Num.'] = str(int(sums))
				sums = 0
				out1Nums.append(j)
				j += 1

		ouT2 = []

		for ot in out1Nums:
			ouT2.append(outL1[ot])

		otCode = ouT2[0]['Qrcd']
		b = otCode.rfind("-")
		newPcb = otCode[28:b]

		k = len(out1Nums)

		if k <= 1 and int(ouT1[0]['Num.']) > ouTsums:
			ouT1[0]['Num.'] = str(a)
			ouT1[0]['coton'] = int(a/int(newPcb))
		elif k <= 1 and int(ouT1[0]['Num.']) == ouTsums:
			del ouT1[0]
		elif k <= 1 and int(ouT1[0]['Num.']) < ouTsums:
			del ouT1[0]
			ouT1[k - 1]['Num.'] = str(a)
			ouT1[k - 1]['coton'] = int(a /int(newPcb))
		else:
			if a > 0:
				del ouT1[0 : (k-1)]
				ouT1[0]['Num.'] = str(a)
				ouT1[0]['coton'] = int(a /int(newPcb))
			else:
				del ouT1[0: k]

		for o in ouT1:
			stockPhs.append(o)

		time1 = time.time()
		time2 =time.localtime(time1)
		outTimes = time.strftime("%Y-%m-%d",time2)
		for ot in ouT2:
			ot['outtime'] = outTimes

		file3 = codecs.open(orderNum +"-"+ stk +"出库" + outTimes +".csv", "w", "utf-8")
		file3.write(str(ouT2))
		file3.close()


		# otCode = ouT2[0]['Qrcd']
		# b = otCode.rfind("-")
		# newPcb = otCode[28:b]
		print("=" * 80)
		print("此批出库品号是：",stk,"出库件数是：",ouTsums/int(newPcb),"出库资讯：")
		print("品号-----------位置------出库件数-------入库时间----------------'Qrcd'")
		global ouT3
		ouT3 = []
		if os.path.isfile("ouTf01stock.data"):
			f = codecs.open("ouTf01stock.data", "r", "utf-8")
			conte = f.read()
			ouT3 = eval(conte)
			f.close()
		else:
			file2 = codecs.open("ouTf01stock.data", "w", "utf-8")
			file2.close()

		for tem in ouT2:
			print("%-12s    %-6s   %-6d   %-22s   %-10s"%(tem['stockID'],tem['Site'],int(tem['Num.'])/int(newPcb),tem['inTime'],tem['Qrcd']))
			tem['order'] = orderNum
			tem['coton'] = int(tem['Num.'])/int(newPcb)
			ouT3.append(tem)

			file5 = codecs.open("ouTf01stock.data", "w", "utf-8")
			file5.write(str(ouT3))
			file5.close()

#删除品号资料，扫描二维码输入，序号删除，需要输入密码方可删除
def delStock():
	# global stockPhs
	password = input("请输入删除密码：")
	if password =="61318":
		shanChu =int(input("请输入删除方式， 1 按品号Qrcd删除  2 按存货序号删除："))
		if shanChu == 1:
			stk = input("请输入要删除的品号Qrcd：")
			print("品号-----------位置------数量-------入库时间----------------'Qrcd'")
			for tem in stockPhs:
				if tem['Qrcd'] == stk:
					print("%-12s    %-6s   %-6s   %-22s   %-10s"%(tem['stockID'],tem['Site'],tem['Num.'],tem['inTime'],tem['Qrcd']))
					outx = stockPhs.index(tem)
					print("准备删除库存表以上第",int(outx) + 1,"序号库存!")
				# time.sleep(1)
					stockPhs.pop(outx)
					print("删除成功！")
		elif shanChu == 2:
			stk2 = int(input("请输入要删除的存货序号："))
			# j=1
			# for tem in stockPhs:
				# print("%-4d    %-12s    %-6s   %-6s   %-22s   %-10s" % (j, tem['stockID'], tem['Site'], tem['Num.'], tem['inTime'], tem['Qrcd']))
				# j+=1
			print("准备删除库存表以上第",stk2,"序号库存!")
			stockPhs.pop(stk2-1)
			print("删除成功！")
	else:
		pass

#显示所有资料
def prtAll():
	print("*"*80)
	print("序号----品号-----------位置------数量-----箱数---------入库时间----------------'Qrcd'")
	print("*"*80)
	Sites =[]
	Hjsites = []
	stockIDs = []
	a = None
	b = None
	siteNum = 0
	stockIDnum = 0
	i = 1
	for tem in stockPhs:
		print("%-4d    %-12s    %-6s   %-6s   %-6s     %-22s   %-10s"%(i,tem['stockID'],tem['Site'],tem['Num.'],tem['coton'],tem['inTime'],tem['Qrcd']))
		a = tem['Site']
		b = tem['stockID']
		i+=1
		if a not in Sites and "H" not in a and "W" not in a:
			Sites.append(a)
		elif a not in Hjsites and "H" in a:
			Hjsites.append(a)
		if b not in stockIDs:
			stockIDs.append(b)
	siteNum = len(Sites)
	hjsiteNum = len(Hjsites)
	stockIDnum = len(stockIDs)
	print("="*60)
	print("目前使用板位是：",siteNum,"个板位！总板位325个，剩余板位：",325-int(siteNum),"个板位！")
	print("目前使用货架是：",hjsiteNum, "个货位！总货位201个，剩余板位：",201 - int(hjsiteNum),"个货位！")
	print("目前在库品号数是：",stockIDnum,"个品号！")

#存档数据
def save2File():
	file2 = codecs.open("stockf01.data","w","utf-8")
	file2.write(str(stockPhs))
	file2.close()
#读取文件
def recoverData():
	global stockPhs
	if os.path.isfile("stockf01.data"):
		f = codecs.open("stockf01.data","r","utf-8")
		conte = f.read()
		stockPhs = eval(conte)
		f.close()
	else:
		file2 = codecs.open("stockf01.data","w","utf-8")
		file2.close()

#品号查询
def nameCx():
	a = int(input("请选择查询方式: 1 是新QRcode全扫描输入查询，2 是键盘输入品号查询："))
	if a == 1:
		# splitQrcd()
		newQr = input("请扫描货物二维码：")
		newName = newQr[16:27]
		print("序号----品号------------位置-----数量-----箱数-------入库时间----------------'Qrcd'")
		j = 1
		sums = 0
		cotons = 0
		for tem in stockPhs:
			if tem['stockID'] == newName:
				print("%-4d    %-12s    %-6s   %-6s   %-6s   %-22s   %-10s"%(j,tem['stockID'],tem['Site'],tem['Num.'],tem['coton'],tem['inTime'],tem['Qrcd']))
				j+=1
				sums = sums + int(tem['Num.'])
				cotons = cotons + int(tem['coton'])

		print("查询结果：品号", newName ,"总库存是：",sums,"pcs.总箱数是：",cotons,"箱！")
	elif a == 2:
		newName = input("请输入查询的品号信息：")
		print("序号----品号------------位置-----数量-----箱数-------入库时间----------------'Qrcd'")
		j = 1
		sums = 0
		cotons = 0
		for tem in stockPhs:
			if tem['stockID'] == newName:
				print("%-4d    %-12s    %-6s   %-6s   %-6s   %-22s   %-10s"%(j,tem['stockID'],tem['Site'],tem['Num.'],tem['coton'],tem['inTime'],tem['Qrcd']))
				j+=1
				sums = sums + int(tem['Num.'])
				cotons = cotons + int(tem['coton'])

		print("查询结果：品号", newName ,"总库存是：",sums,"pcs.总箱数是：",cotons,"箱！")

#库龄查询及制令追溯查询
def stockDatecx():
	a = int(input("请选择查询方式: 1 库龄查询，2 是制令追溯查询：3 是出库日期查询：9 是确认贴标资讯："))
	if a == 1:
		stockDate = int(input("请输入要查询的库龄天数："))
		print("*"*80)
		print("序号----品号-----------位置------数量-----箱数-------入库时间----------------'Qrcd'")
		print("*"*80)

		timea = time.time()
		# nowTime = time.mktime(time.strptime(timea, '%Y-%m-%d'))
		Sites = []
		stockIDs = []
		Hjsites =[]
		i = 1
		sums = 0

		for tem in stockPhs:
			k = int(timea - time.mktime(time.strptime(tem['inTime'], '%Y-%m-%d %H:%M:%S')))/(24*60*60)
			if k > stockDate:
				print("%-4d    %-12s    %-6s   %-6s   %-6s  %-22s   %-10s"%(i,tem['stockID'],tem['Site'],tem['Num.'],tem['coton'],tem['inTime'],tem['Qrcd']))
				a = tem['Site']
				b = tem['stockID']
				sums = sums + int(tem['Num.'])
				i+=1
				if a not in Sites and "H" not in a:
					Sites.append(a)
				if a not in Hjsites and "H" in a:
					Hjsites.append(a)
				if b not in stockIDs:
					stockIDs.append(b)
		siteNum = len(Sites)
		Hjsitenum = len(Hjsites)
		stockIDnum = len(stockIDs)
		print("="*80)
		print("目前库龄超过",stockDate,"天的占用板位是：",siteNum,"个板位！",Hjsitenum,"个货架位！")
		print("目前库龄超过",stockDate,"天的品号数是：",stockIDnum,"个品号！")
		print("目前库龄超过",stockDate, "天的总库存量是：",sums, "pcs")
	elif a == 2:
		global ouT3
		zhiling = input("请输入要查询的制令：")
		f2 = codecs.open("ouTf01stock.data", "r", "utf-8")
		conte = f2.read()
		ouT3 = eval(conte)
		f2.close()
		print("品号----------出库位置---数量-----箱数----------入库时间------------------'Qrcd'----------------------------'order'")
		for tem in ouT3:
			if tem['Qrcd'][0:15] == zhiling:
				print("%-12s    %-6s   %-6s  %-6s   %-22s   %-10s    %-10s" % (tem['stockID'], tem['Site'], tem['Num.'], tem['coton'], tem['inTime'], tem['Qrcd'], tem['order']))
			else:
				continue
	elif a == 3:
		chukuRiqi = input("请输入要查询的出库日期 ，格式%Y-%m-%d：")
		f5 = codecs.open("ouTf01stock.data", "r", "utf-8")
		conte = f5.read()
		ouT3 = eval(conte)
		f5.close()
		print("品号----------出库位置---数量-----箱数----------入库时间------------------'Qrcd'----------------------------'order'-----------出库日期")
		for tem in ouT3:
			if str(tem['outtime']) == chukuRiqi:
				print("%-12s    %-6s   %-6s  %-6s   %-22s   %-10s    %-10s    %-10s" % (tem['stockID'], tem['Site'], tem['Num.'] ,tem['coton'], tem['inTime'], tem['Qrcd'],tem['order'],str(tem['outtime'])))
			else:
				continue
	elif a == 9:
		erWeima = input("请扫描要贴标的二维码：")
		time1 = time.time()
		time2 = time.localtime(time1)
		outTimes = time.strftime("%Y-%m-%d", time2)
		f5 = codecs.open("ouTf01stock.data", "r", "utf-8")
		conte = f5.read()
		ouT3 = eval(conte)
		f5.close()
		chuKus =[]
		print("品号----------出库位置---数量-----箱数----------入库时间------------------'Qrcd'----------------------------'order'-----------出库日期")
		for tem in ouT3:
			if tem['Qrcd'][:15] == erWeima[:15]:
				chuKus.append(tem)
				for tem2 in chuKus:
					if str(tem2['outtime']) == outTimes:
						print("%-12s    %-6s   %-6s  %-6s   %-22s   %-10s    %-10s    %-10s" % (tem['stockID'], tem['Site'], tem['Num.'] ,tem['coton'], tem['inTime'], tem['Qrcd'],tem['order'],str(tem['outtime'])))
			else:
				print("贴标错误，未按要求贴标，请确认位置是否正确！")
				break

def passWord():
	i = 1
	while i <= 3:
		password = input("请输入登陆密码：")
		if password !="61318":
			i += 1
			while i < 4:
				print("密码错误，请重新输入，你还有",4-i ,"次机会！")
			else:
				print("您无权限登陆，请联络系统管理员，谢谢使用！")
				break
		else:
			print("登陆成功，欢迎使用GF看板系统！")
# 主函数
def main():
	i = 1
	while i <= 3:
		password = input("请输入登陆密码：")
		if password != "61318" and password != "0":
			i += 1
			if i < 4:
				print("密码错误，请重新输入，你还有", 4 - i, "次机会！")
			else:
				print("您无权限登陆，请联络系统管理员，谢谢使用！")
				break
		elif password == "0":
			break
		else:
			print("登陆成功，欢迎使用GF看板系统！")
			#读取之前的数据
			recoverData()
			while True:
				printMenu()
			#功能选择
				key = input("请输入你要选择的功能的数字：")
				if key == "1":
					newInfo()
					save2File()
					# while True:
					# 	if input("请确认是否继续入库: 0 退出，1 继续 ") == "1":
					# 		newInfo()
					# 		save2File()
					# 	else:
					# 		break
				elif key == "2":
					modifInfo()
					save2File()
				elif key == "3":
					siteCx()
					save2File()
				elif key == "4":
					delStock()
					save2File()
				elif key == "5":
					prtAll()
					time.sleep(5)
					hwxsGn.Hwxs()
				elif key == "6":
					save2File()
				elif key == "7":
					nameCx()
				elif key == "8":
					ouTstock()
					save2File()
					# while True:
					# 	if input("请输入 1 继续出库, 0 退出出库界面：") == "1":
					# 		ouTstock()
					# 		save2File()
					# 	else:
					# 		break
				elif key == "9":
					stockDatecx()
				elif key == "0":
					break
main()
