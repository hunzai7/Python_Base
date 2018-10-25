# -*- coding:utf-8 -*-
# Project： python基础
# File: 文件读取.py
# Author: Hunzai
# Time: 2018/10/17 14:48
# Digest: None

f = open("C:\\Users\Hunzai\Desktop\大数据学习规划.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    print(line)
    if len(line) == 0:
        break
f.close()


