# -*- coding:utf-8 -*-
# Project： python基础
# File: 中断语句.py
# Author: Hunzai
# Time: 2018/10/17 10:50
# Digest: None

'''continue中断一次，break中断循环'''

for i in range(0, 5):
    if i == 2:
        continue
    print("Hello ", i + 1)

print("\033[32;1m===========\033[0m")

for i in range(0, 5):
    if i == 2:
        break
    print("Hello ", i + 1)
