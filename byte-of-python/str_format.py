#!/usr/bin/python
# coding:utf-8

age = 20
name = 'imhet'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 111
print('{0:_^111}'.format('hello'))

# 基于关键词输出 'imhet wrote A Byte of Python'
print('{name} wrote {book}'.format(book='A Byte of Python' , name='imhet'))

# print 总是会以一个不可见的“新一行”字符（\n）结尾，因此重复调用 print将会在相互独立的一行中分别打印。为防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('a', end='')
print('b', end='')

print('a', end=' ')
print('b', end=' ')
print('c')

print('This is the first line\nThis is the second line')

print("This is the first sentence.\
      This is the second sentence.")

# 如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加 r 或 R 来指定一个 原始（Raw） 字符串
print(r"Newlines are indicated by \n")
