import os
import time
import math

stockPhs = []
#定义主界面显示函数
def printMenu():
	print("="*60)
	print("群福塑胶制品有限公司仓库看板系统")
	print("1.仓库入库功能")
	print("2.修改仓库存货功能")
	print("3.仓位查询存货功能")
	print("4.删除存货功能")
	print("5.展示仓库存货品号信息")
	print("6.存档功能")
	print("7.品号查询存货功能")
	print("8.出库管理功能")
	print("9.退出仓库看板系统")
	print("="*60)

def splitQrcd():
	a = input("请扫描货物二维码：")
	newName = a[16:27]
	b = a.findr("-")
	newPcb = a[29:b]
	return newName
	return newPcb
	print(newName,"包装是：",newPcb)

#定义新增品号函数
def newInfo():
	newQr = input("请扫描货物二维码：")
	newName = input("请输入新入的品号信息：")
	newSite = input("请输入存货位置信息：")
	newNum = input("请输入入库数量信息：")
	timea = time.time()
	timeArray = time.localtime(timea)

	stockPh = {}
	
	stockPh['品号'] = newName
	stockPh['位置'] = newSite
	stockPh['数量'] = newNum
	stockPh['时间'] = time.strftime("%Y--%m--%d %H:%M:%S",timeArray)
	stockPh['Qrcd'] = newQr
	stockPhs.append(stockPh)

#修改存货功能
def modifInfo():
	stoId = int(input("请输入需要修改存货序号："))
	newQr = input("请扫描货物二维码：")
	newName = input("请输入新入的品号信息：")
	# newName = mid(newQr,1,6)
	newSite = input("请输入存货位置信息：")
	newNum = input("请输入入库数量信息：")

	stockPhs[stoId-1]['Qrcd'] = newQr 
	stockPhs[stoId-1]['品号'] = newName
	stockPhs[stoId-1]['位置'] = newSite
	stockPhs[stoId-1]['数量'] = newNum


#位置查询存货功能
def siteCx():
	a = input("请输入查询存货位置：")
	print("序号---品号---位置---数量---时间--Qrcd")
	j = 1
	for tem in stockPhs:
		if tem['位置'] == a:
			print("%d   %s   %s  %s  %s  %s"%(j,tem['品号'],tem['位置'],tem['数量'],tem['时间'],tem['Qrcd']))
			j+=1
#出库功能，待修改FIFO功能
def ouTstock():
	# global stockPhs
	stk = input("请输入要出库的品号：")
	sums = int(input("请输入出库数量："))
	print("序号---品号---位置---数量---时间--Qrcd")
	j = 1
	a = None
	for tem in stockPhs:
		if tem['品号'] == stk:
			print("%d   %s     %s     %s   %s    %s"%(j,tem['品号'],tem['位置'],tem['数量'],tem['时间'],tem['Qrcd']))
			outx = stockPhs.index(tem)
			if int(tem['数量']) <= sums:
				sums = sums -int(tem['数量'])
				stockPhs.pop(outx)
				if sums > 0:
					j+=1
					continue
				else:
					break
			elif int(tem['数量']) > sums :
				a = int(tem['数量']) -sums
				sums == 0
				if a > 0:
					stockPhs[outx]['数量'] = str(a)
					j+=1
					break
			# j+=1	
	print("品号----------出库完成！")

#删除品号资料，扫描二维码输入
def delStock():
	# global stockPhs
	stk = input("请输入要删除的品号Qrcd：")
	for tem in stockPhs:
		if tem['Qrcd'] == stk:
			print("%s     %s     %s   %s    %s"%(tem['品号'],tem['位置'],tem['数量'],tem['时间'],tem['Qrcd']))
			outx = stockPhs.index(tem)
			print("准备删除库存表第",int(outx) + 1,"序号库存!")
		time.sleep(1)
	stockPhs.pop(outx)
	print("删除成功！")
	
#显示所有资料
def prtAll():
	print("*"*30)
	print("序号---品号---位置---数量---时间---'Qrcd'")
	print("*"*30)
	i = 1
	for tem in stockPhs:
		print("%d    %s    %s   %s   %s   %s"%(i,tem['品号'],tem['位置'],tem['数量'],tem['时间'],tem['Qrcd']))
		i+=1
#存档数据
def save2File():
	file2 = open("stock.data","w")
	file2.write(str(stockPhs))
	file2.close()
#读取文件
def recoverData():
	global stockPhs
	f = open("stock.data","r")
	conte = f.read()
	stockPhs = eval(conte)
	# print(stockPhs)
	f.close()



#品号查询
def nameCx():
	a = input("请输入查询品号：")
	print("序号---品号---位置---数量---时间--Qrcd")
	j = 1
	sums = 0
	for tem in stockPhs:
		if tem['品号'] == a:
			print("%d       %s     %s     %s   %s  %s"%(j,tem['品号'],tem['位置'],tem['数量'],tem['时间'],tem['Qrcd']))
			j+=1
			sums = sums + int(tem['数量'])

	print("品号",a,"总库存是：",sums)


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
			break


main()