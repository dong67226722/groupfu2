econding = "utf-8"
import os
import time
import math
import codecs

stockPhs = []
#定义主界面显示函数
def printMenu():
	print("="*80)
	print("群福塑胶制品有限公司仓库看板系统")
	print("1.仓库入库功能")
	print("2.修改仓库存货功能")
	print("3.仓位查询存货功能")
	print("4.删除存货功能")
	print("5.展示仓库存货品号信息")
	print("6.存档功能")
	print("7.品号查询存货功能")
	print("8.出库管理功能")
	print("9.存货库龄查询功能")
	print("0.退出仓库看板系统")
	print("="*80)

def splitQrcd():
	a = input("请扫描货物二维码：")
	newName = a[16:27]
	b = a.rfind("-")
	newPcb = a[28:b]
	return newName
	return newPcb
	# print(newName,"包装是：",newPcb)

def stockFifo():
	pass




#定义新增品号函数
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
		newSite = input("请输入存货位置信息：")
		newNum = input("请输入入库数量信息：")
		print("此批入库资讯是：","品号：",newName,"数量：",newNum,"位置是：",newSite)

	timea = time.time()
	timeArray = time.localtime(timea)

	stockPh = {}
	
	stockPh['stockID'] = newName
	stockPh['Site'] = newSite
	stockPh['Num.'] = newNum
	stockPh['inTime'] = time.strftime("%Y--%m--%d %H:%M:%S",timeArray)
	stockPh['Qrcd'] = newQr
	stockPhs.append(stockPh)

#修改存货功能
def modifInfo():
	stoId = int(input("请输入需要修改存货序号："))
	# newInfo()
	newQr = input("请扫描货物二维码：")
	newName = input("请输入新入的品号信息：")
	newSite = input("请输入存货位置信息：")
	newNum = input("请输入入库数量信息：")

	stockPhs[stoId-1]['Qrcd'] = newQr 
	stockPhs[stoId-1]['stockID'] = newName
	stockPhs[stoId-1]['Site'] = newSite
	stockPhs[stoId-1]['Num.'] = newNum


#位置查询存货功能
def siteCx():

	a = input("请输入查询存货位置：")
	print("序号----品号-----------位置------数量----------入库时间----------------'Qrcd'")
	j = 1
	for tem in stockPhs:
		if tem['Site'] == a:
			print("%d   %s   %s  %s  %s  %s"%(j,tem['stockID'],tem['Site'],tem['Num.'],tem['inTime'],tem['Qrcd']))
			j+=1
#出库功能，待修改FIFO功能
def ouTstock():
	global stockPhs
	stk = input("请输入要出库的品号：")
	sums = int(input("请输入出库数量："))
	print("序号----品号-----------位置------数量----------入库时间----------------'Qrcd'")
	ouTstocks = []
	for tem in stockPhs:
		if tem['stockID'] == stk and tem not in ouTstocks:
			ouTstocks.append(tem)
			outx = stockPhs.index(tem)
			stockPhs.pop(outx)
	ouT1 = sorted(ouTstocks, key=lambda s: s['inTime'])
	j = 0
	adNum = len(ouT1)
	for j in range(adNum):
		if int(ouT1[j]['Num.']) <= sums:
			sums = sums - int(ouT1[j]['Num.'])
			ouT1.pop(j)
			j+=1
			continue
		elif int(ouT1[j]['Num.']) > sums:
			a = int(ouT1[j]['Num.']) - sums
			sums = 0
			if a > 0:
				ouT1[j]['Num.'] = str(a)
			break
	print(ouT1)
	for o in ouT1:
		stockPhs.append(o)
#删除品号资料，扫描二维码输入
def delStock():
	# global stockPhs
	stk = input("请输入要删除的品号Qrcd：")
	for tem in stockPhs:
		if tem['Qrcd'] == stk:
			print("%s     %s     %s   %s    %s"%(tem['stockID'],tem['Site'],tem['Num.'],tem['inTime'],tem['Qrcd']))
			outx = stockPhs.index(tem)
			print("准备删除库存表第",int(outx) + 1,"序号库存!")
		time.sleep(1)
	stockPhs.pop(outx)
	print("删除成功！")
	
#显示所有资料
def prtAll():
	print("*"*80)
	print("序号----品号-----------位置------数量----------入库时间----------------'Qrcd'")
	print("*"*80)
	Sites =[]
	stockIDs = []
	a = None
	b = None
	siteNum = 0
	stockIDnum = 0
	i = 1
	for tem in stockPhs:
		print("%-4d    %-12s    %-6s   %-6s   %-22s   %-10s"%(i,tem['stockID'],tem['Site'],tem['Num.'],tem['inTime'],tem['Qrcd']))
		a = tem['Site']
		b = tem['stockID']
		i+=1
		if a not in Sites:
			Sites.append(a)
		if b not in stockIDs:
			stockIDs.append(b)
	siteNum = len(Sites)
	stockIDnum = len(stockIDs)
	print("="*30)
	print("目前使用板位是：",siteNum,"个板位！总板位568个，剩余板位：",568-int(siteNum),"个板位！")
	print("目前在库品号数是：",stockIDnum,"个品号！")
#存档数据
def save2File():
	file2 = codecs.open("stock.data","w","utf-8")
	file2.write(str(stockPhs))
	file2.close()
#读取文件
def recoverData():
	global stockPhs
	f = codecs.open("stock.data","r","utf-8")
	conte = f.read()
	stockPhs = eval(conte)
	# print(stockPhs)
	f.close()



#品号查询
def nameCx():
	a = input("请输入查询品号：")
	print("序号----品号-----------位置------数量----------入库时间----------------'Qrcd'")
	j = 1
	sums = 0
	for tem in stockPhs:
		if tem['stockID'] == a:
			print("%-4d    %-12s    %-6s   %-6s   %-22s   %-10s"%(j,tem['stockID'],tem['Site'],tem['Num.'],tem['inTime'],tem['Qrcd']))
			j+=1
			sums = sums + int(tem['Num.'])

	print("品号",a,"总库存是：",sums)
	return sums


# 主函数
def main():
#读取之前的数据
	recoverData()
	while True:
		printMenu()

	#功能选择
		key = input("请输入你要选择的功能的数字：")
		if key == "1":
			newInfo()
			save2File()
		elif key == "2":
			modifInfo()
			save2File()
		elif key == "3":
			siteCx()
		elif key == "4":
			delStock()
			save2File()
		elif key == "5":
			prtAll()
		elif key == "6":
			save2File()
		elif key == "7":
			nameCx()
		elif key == "8":
			ouTstock()
			save2File()
		elif key == "9":
			pass
		elif key == "0":
			break
	
main()