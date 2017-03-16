# 对象自省

import inspect


# dir
my_list = [1, 2, 3]
print(dir(my_list))


# type
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))


# id
name = "Yasoob"
print(id(name))


# inspect模块也提供了许多有用的函数，来获取活跃对象的信息。比方说，你可以查看一个对象的成员
print(inspect.getmembers(str))
