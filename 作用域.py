# -*- coding:utf-8 -*-
# Project： python基础
# File: 作用域.py
# Author: Hunzai
# Time: 2018/10/17 11:39
# Digest: 全局变量和局部变量

i = 10


def func1():
    global j
    j = 10


func1()
print(j)


#  局部变量
def func2():
    z = 20
