# -*- coding:utf-8 -*-
# Author:Mr.Xu

'''
while True:
    a = int(input('a:'))
    print(type(a))
    if a==1:print('a:',a)
'''

array = [1, 3, 5]
array2 = []

#冒泡 逐次对比
# for i in range(len(array)):
#     for j in range(len(array)-1-i):
#         if array[j] < array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]

#选择 将第i个和后面的对比
# for i in range(len(array)-1):
#     for j in range(i+1, len(array)):
#         if array[i] < array[j]:
#             array[i], array[j] = array[j], array[i]



print('array:', array)
