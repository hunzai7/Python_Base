# -*- coding:utf-8 -*-
# Project： python基础
# File: 异常.py
# Author: Hunzai
# Time: 2018/10/22 21:02
# Digest: None

import urllib.request as request

for i in range(0, 100):
    try:
        file = request.urlopen("https://www.hellobi.com",timeout=0.5)
        data = file.read()
        print(len(data),i)
    except Exception as e:
        print("error:" + str(e))
