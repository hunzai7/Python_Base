# -*- coding:utf-8 -*-
# Author:Mr.Xu

import copy

#key-value
info={
    'name':'Mex',
    'age':'12',
    'salary':'18000',
    'gender':'man'
}
info2 = copy.deepcopy(info);

print(info)

info['name'] = 'hunzai'
print(info)

#del
#del info['salary']
info.pop('gender')
info.popitem() #随机删除
print(info)

print("-----------------------------")

'''
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog.setdefault("大陆",{"www.baidu.com":[1,2]}) #如果有字段，不做修改，如果没有设置该字段
print(av_catalog)
'''

info3 = {
    'name':'Mex',
    'age':12
}
new = {
    'name':'hunzai',
    'salary':18000
}
info3.update(new)
print(info3)
print(info3.items())

c = info3.fromkeys([3,4,5],[{'name':'hunzai'},'b','c'])
c[3][0]['name'] = 'Max'
print(c)

for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)

for index,item in enumerate(info3):
    print(index,item)