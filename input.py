# -*- coding:utf-8 -*-
# Author:Mr.Xu

name = input("Please input your name:")
age = int(input("Please input your age:"))
print(type(age))

print("name:",name,",age:",age)

# info = '''
# ------------- info of ''' + name + '''-----------
# Name:''' + name + '''
# Age:''' + age

info2 = '''
--------------info2 of %s-------------
Name:%s
Age:%d
''' %(name,name,age)
print(info2)

info3 = '''
--------------info3 of {_name}-------------
Name:{_name}
Age:{_age}
'''.format(_name = name,
           _age= age)
print(info3)

info4 = '''
--------------info4 of {0}-------------
Name:{0}
Age:{1}
'''.format(name,name,age)
print(info4)
