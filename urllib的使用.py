# -*- coding:utf-8 -*-
# Project： python基础
# File: urllib的使用.py
# Author: Hunzai
# Time: 2018/10/22 20:38
# Digest: None

import urllib.request as request

'''urlretrieve'''
'''request.urlretrieve("https://www.hellobi.com",filename="通过urlretrieve下载的网页.html")'''


'''urlcleanup'''
request.urlcleanup()


'''info'''
file = request.urlopen("https://www.hellobi.com")
# 网页信息
print(file.info())
# 网页状态
print(file.getcode())
# 网页地址
print(file.geturl())


# timeout超时设置
# request.urlopen("https://www.hellobi.com",timeout=0.1)


