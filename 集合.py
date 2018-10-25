# -*- coding:utf-8 -*-
# Author:Mr.Xu

list_1 = [1,2,4,66,8,12,9,2,5,8,12]
list_1 = set(list_1)

print("list_1",list_1)

list_2 = [1,2,4,56,78,3]
print("list_2",list_2)

# 交集
print("交集",list_1.intersection(list_2))

# 并集
print("并集",list_1.union(list_2))

# 差集
print("差集",list_1.difference(list_2))

# 对称差集
print("反向差集",list_1.symmetric_difference(list_2))

# 子集
print("子集",list_1.issubset(list_2))

# 父集
print("父集",list_1.issuperset(list_2))

print("\n-----------------------------------------\n")

list_3 = set([1,2,3,4])
list_4 = set([2,3,5,6])
print("list_3",list_3)
print("list_4",list_4)

print('&',list_3 & list_4)
print('|',list_3 | list_4)
print('-',list_3 - list_4)
print('^',list_3 ^ list_4)