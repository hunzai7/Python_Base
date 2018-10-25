# -*- coding:utf-8 -*-
# Project： python基础
# File: 1+2.py
# Author: Hunzai
# Time: 2018/10/18 8:19
# Digest: None

import xlrd, xlsxwriter

# 需要处理的文件
allxls = ["1.xlsx", "2.xlsx"]

# 合并后的文件
endxls = "end.xlsx"


def open_xlsx(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("Open error,error factor : " + e)


# 获取所有sheet
def getsheet(fh):
    return fh.sheets()


# 读取当前sheet的行数
def getnrows(fh, sheet):
    table = fh.sheets()[sheet]
    content = table.nrows
    return content


# 读取文件内容并返回所有行的值
def getfilect(fh, file, shnum):
    fh = open_xlsx(file)
    table = fh.sheet_by_name(shname[shnum])
    num = getnrows(fh)
    lenrvalue = len(rvalue)
    for row in range(0, num):
        rdata = table.row_values(row)
        rvalue.append(rdata)
    filevalue.append(rvalue[lenrvalue])
    return filevalue


# 存储所有读取数据
filevalue = []
# 存储一个标签的结果
svalue = []
# 存储一行结果
rvalue = []
# 存储各sheet名
shname = []

# 读取第一个待读文件，获得sheet数
fh = open_xlsx(allxls[0])
sh = getsheet(fh)
x = 0
for sheet in sh:
    shname.append(sheet.name)
    svalue.append([])
    x += 1

# 依次读取各sheet的内容
# 依次读取当前sheet的内容
for shnum in range(0, x):
    for fl in allxls:
        print("Reading NO." + str(fl) + " sheet's context ...")
        filevalue = getfilect(fh, fl, shnum)
    svalue[shnum].append(filevalue)

# 由于append具有叠加关系，分析可得所有信息均在svalue[0][0]中存储
# svalue[0][0]元素数量为sheet便签数(sn)*文件数(fn)
sn = x
fn = len(allxls)
endvalue = []


# 设置一个函数专门获取svalue里面的数据，即获取各项标签的数据
def getvalue(k):
    for z in range(k, k + fn):
        endvalue.append(svalue[0][0][z])
    return endvalue

# 打开最后编写的文件
wb1 = xlsxwriter.Workbook(endxls)
# 创建一个sheet工作对象
ws = wb1.add_worksheet()
polit=0
linenum=0
# 依次遍历每个sheet中的数据
for s in range(0,sn*fn,fn):
    thisvalue=getvalue(s)
    tvalue = thisvalue[polit:]
    for a in range(0,len(tvalue)):
        for b in range(0,len(tvalue[a])):
            for c in range(0,len(tvalue[a][b])):
                print(linenum)
                print(c)
                data=tvalue[a][b][c]
                ws.write(linenum,c,data)
            linenum +=1
    # 叠加关系，需要设置分割点
    polit=len(thisvalue)
wb1.close()