# -*- coding:utf-8 -*-
# Project： python基础
# File: 乘法口诀表.py
# Author: Hunzai
# Time: 2018/10/17 10:58
# Digest: None

for i in range(1, 10):
    for j in range(1, i + 1):
        # end=""，控制不换行
        print(str(j) + "*" + str(i) + "=" + str(i * j)+"\t\t",end="")
    print()
