# -*- coding:utf-8 -*-
# Author:Mr.Xu

name = "my name is \tMax"
print(name.count("a"))
print(name.center(40, '*'))
print(name.capitalize())
print(name.endswith("ax"))
print(name.expandtabs(tabsize=10))

name2 = "my name is {name},and my age is {age}"
print(name2.format(name="Max", age="12"))
print(name2.format_map({'name': 'Min', 'age': '11'}))
print(name2.index("age"))
print(name2[25].isalnum())

print('ccc'.isalpha())  # 是否全是字母
print("12223".isdecimal())
print("12223".isdigit())

print("!string".isidentifier())  # 是否是一个合法的标志符
print("33".isnumeric())

print("May Is A Month".istitle())  # 标题判断（每个单词首字母大写）

print("hello".join("--"))
print("hunzai".ljust(10, "*"))
print("hunzai".rjust(10, "*"))

print("\nhunzai lang".lstrip())
print("hunzai lang\n".rstrip())
print("--")
print("     hunzai\n".strip())

p = str.maketrans("abc", "123")  # 替换对应下标的内容
print("hunzai lang".translate(p))

print("hunzai".replace("a", "1"))
print("hunzai hunizai".rfind("i"))  # 最后一次出现的下标

print('1，2，3'.split(","))
print('1\n2\n3'.splitlines())

print("hunzai lang".swapcase())
print("hunzai lang".title())
print("hunzai lang".zfill(20))  # 类似于rjust和ljust

print("hunzai lang".count("a"))
