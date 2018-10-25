# -*- coding:utf-8 -*-
# Project： python基础
# File: 模拟爬虫正则.py
# Author: Hunzai
# Time: 2018/10/20 15:20
# Digest: 测试正则

import re

string = '<a href="https://www.baidu.com"></a>'
pat1 = "\"(.*)\""
pat2 = "[a-zA-Z]+://[^\s]*[com|cn]"  # \w+://.*[com|cn] 或者 \w+://\S*[com|cn]
rst1 = re.compile(pat1).findall(string)
rst2 = re.compile(pat2).findall(string)
print(rst1)
print(rst2)