# -*- coding:utf-8 -*-
# Project： python基础
# File: for循环.py
# Author: Hunzai
# Time: 2018/10/17 10:42
# Digest: None

a = ["a","b","c","d"]

for i in a:
    print(i)

# 重复执行5次，等同(i=0;i<5;i++)
for i in range(0,5):
    print("Hello ",i+1)