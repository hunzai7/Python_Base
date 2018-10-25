# -*- coding:utf-8 -*-
# Project： python基础
# File: 正则表达式.py
# Author: Hunzai
# Time: 2018/10/20 11:11
# Digest: 基本的正则表达式

import re

'''
    元字符：
        \w: 匹配所有字符包括下划线
        \d: 匹配所有数字
        \s: 匹配所有不可见字符
        \W: 匹配所有非字符
        \D: 匹配所有非数字
        \S: 匹配所有可见字符
        [^a]: 不匹配a
        [abc]: 匹配[]中任意字符
        *: 匹配任意次数前缀字符
        ?: 匹配0次或1次前缀字符
        +: 匹配1次或多次前缀字符，不包括零次
        {n}: 匹配n次连在一起的前缀字符
        .: 匹配除了换行符以外的任意字符
    
    模式修正符:
        I:  忽视大小写
        M:  多行匹配
        L:  本地化匹配
        U:  unicode匹配
        
    贪婪模式和懒惰模式：
        a.*b: 贪婪模式,一直匹配到最后
        a.*?b: 懒惰模式,匹配到第一个即结束
        
'''

'''
string = "python"
pat = "[^y]{4}"
print(re.search(pat,string))

string0 = "python"
pat0 = "\wth\w"
print(re.search(pat0,string0))


string1 = "python"
pat1 = "th[ona]n"
print(re.search(pat1,string1))


string2 = "string"
string3 = "sssatring"
pat2 = "s*"
pat3 = "s*ah*"
print(re.search(pat2,string2))
print(re.search(pat3,string3))


string4 = "string"
string5 = "tring"
pat4 = "s?"
pat5 = "s?"
print(re.search(pat4,string4))
print(re.search(pat5,string5))

string6 = "pythhhon"
pat6 = "th+"
print(re.search(pat6,string6))


string7 = "pythhhon"
pat7 = "th{2}"
print(re.search(pat7,string7))

string8 = "qdqdpythoncfalnjoi"
pat8 = ".python..."
print(re.search(pat8,string8))
'''

'''
pat1 = "python"
pat2 = "python"
string = "anuanoasdPythonasid"
print("无模式修正：",re.search(pat1,string))
print("模式修正：",re.search(pat2,string,re.I))
'''

'''
string = "nihaooobadanfojdab"
pat = "a.*?b"
pat2 = "a.*b"
print(re.search(pat, string))
print(re.search(pat2, string))
'''

#  match从字符串头部开始匹配
string = "hunzaiqichongtian"
pat = "h.*?i"
print(re.match(pat,string))

#  匹配所有字符串
string = "hunzaiqichongtianhunzaibachongtian"
pat = "h.*?i"
print(re.compile(pat).findall(string))