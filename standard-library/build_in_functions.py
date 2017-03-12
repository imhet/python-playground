# python 内置函数使用，部分函数因为相近例子写在了一起


# abs 绝对值
# pow 乘方
# round
# sum
print(abs(-3))
print(abs(3.0))
print(abs(3 + 4j))
print(pow(2, 10))
print(pow(2, 10, 10))   # pow(a,b,c) = pow(a,b) % c
print(round(2.675, 2))
print(round(2.676, 2))
print(sum(range(0, 101)))


# all
print()
print(all([1, 2, 3]))
print(all([]))


# any
print()
print(any([1, 2]))
print(any([]))


# ascii
print()
print(ascii('dd-&*^-'))
print(ascii(123))


# bin 二进制格式
print()
print(bin(123))
print(bin(-8))


# bool
print()
print(bool(-8))
print(bool(8))
print(bool(0))
print(bool([]))
print(bool([1]))
print(bool(''))
print(bool('a'))


# bytearray
print()
print(bytearray('dddddddad', 'utf-8'))
print(bytearray(1))


# bytes
print()
print(bytes('dddddddad', 'utf-8'))
print(bytearray(1))


# callable
print()
print(callable(1))


# chr 转化为 unicoder 字符串
# ord 则相反
print()
print(chr(97))
print(ord('a'))
print(chr(8364))
print(ord('€'))
# must by <= 1114111
# print(chr(11141111))


# classmethod 类方法
# staticmethod 静态方法
print()
class A:
    @classmethod
    def hello(self):
        print('hello')

A().hello()
A.hello()


# 强大的compile 函数，编译为字节代码对象，参见 http://blog.csdn.net/caimouse/article/details/41049949
# exec 动态执行 python 代码
# exec('for i in range(0,10): print(i,end='')')
print()
str1 = "for i in range(0,10): print(i,end='')"
c = compile(str1, '', 'exec')
exec(c)
# 还可以编译为表达式
str2 = "3*x + 4*y"
c2 = compile(str2, '', 'eval')
print(c2)


# 复数，如果是从字符串转化而来+/-操作符前后不能有空格
print()
print(complex(1+9j))
print(complex('1+9j'))
print(abs(complex(1+9j)))


# getattr 获取类的属性
# setattr 给类设置属性
# hasattr 类是否有某属性
# delattr 删除类的某个属性
# 参见 http://www.cnblogs.com/zhangjing0502/archive/2012/05/16/2503702.html
print()
print(getattr(A(), 'hello', 'not found'))
setattr(A, 'het', 123)
print(hasattr(A, 'het'))
print(A().het)
delattr(A, 'het')
print(hasattr(A, 'het'))


# 列出对象/模块的类、方法和成员变量
print()
print(dir())
print(dir([1, 2]))


# 返回两个数的商和余数的元组 divmod(x,y) = (x//y, x%y)
# 如果 x y 是浮点数 相当于 divmod(x,y) = (math.floor(a/b), a%b)
print()
print(divmod(3, 4))
print(divmod(4, 2))
print(divmod(1, 0.3))
print(divmod(0.3, 1))


# enumerate，获取可迭代（可遍历）对象的索引和值
print()
for i, key in enumerate('abcde'):
    print(i, key)


# eval 执行字符串表达式并返回表达式的值 ; 可以指定 global 和 local 作用域
print()
print(eval('1+2+3'))
g = {'a': 1, 'b': 20}
l = {'a': 21, 'b': 12}
print(eval('a + b', g, l))



# filter 用传入的函数过滤指定序列
# 等价于 item for item in iterable if function(item)
# function 为 none 时，等价于 item for item in iterable if item
# map 对序列中每个元素都执行函数
# zip 它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）
print()


def is_even(x): return x & 1 != 0
for i in filter(is_even, [1, 2, 3, 4, 5]):
    print(i, end=' ')

print()


def cube(x):
    print(x*x*x)

map(cube, range(1, 11))

a = [1, 2, 3]
b = [4, 5, 6]
print(dict(zip(a, b)))



# float 把数字或者字符串转化为浮点数
print()
print(float('+1.23'))
print(float('   -12345\n'))
print(float('1e-003'))
print(float(1e-003))
print(float('+1E6'))
print(float('-Infinity'))


# format 字符串格式化    https://docs.python.org/3/library/string.html#formatspec
print()
print('{0} is {1} years old. '.format('het', 20))
print('{first} is as {second}. '.format(second='hello', first='world'))  # 别名替换
print('{0:.3} is a decimal. '.format(1 / 3))  # 小数点后3位
print('{0:_^11} is a 11 length. '.format('het'))  # 填充对齐，使用_补齐空位
print('My name is {0:8}.'.format('Fred'))  # 填充，指定宽度
print('My name is {0.name}'.format(open('out.txt', 'w')))  # 调用方法
print('{a[5]}'.format(a=range(10)))  # 下标
print('{:b}'.format(17))   # 进制转化，b d o x 分别代表二进制 十进制 八进制 十六进制
print('{:,}'.format(1234567890))   # 金额的千位分隔符


# frozenset 创建不可变的集合；不可向该集合添加/删除元素，存在哈希值,可以作为字典的 key
# set 相反
print()
a = frozenset(['1', '2'])


# globals 返回全局变量的字典，可修改
# locals 返回局部变量的字典，不可修改
# vars 返回对象属性和属性值的 dict
print()
# print(locals())
# print(globals())
# print(vars())


# hash 返回字符串或数字的 hash 值 ； 注意：字符串的 hash 值每次运行可能都不一样
print()
print(hash('a'))
print(hash('b'))
print(hash(1))
print(hash(1.0))


# help 帮助文档，多用能进步
print()
# help(list)


# hex 把整数转化为小写的16进制并以'0x'开头
# oct 把整数转化为小写的8进制并以'0o'开头
print()
print(hex(255))
print(hex(-255))
print(oct(255))
print(oct(-255))
# 浮点数的 hex ，不能用内置函数，必须用 float 的 hex 函数
a = 1.0
print(a.hex())


# id 对象的唯一标识
print()
print(id(1))
print(id('1'))


# input 用于输入
# input('abc')


# int 转化为整数
# 如果带第2个参数，意味着第1个参数的进制是第2个参数，使用 int 将会把把该数转化为10进制的整数
print()
print(int('111'))
print(int(11.0))
print(int('12', 16))
print(int('0xa', 16))


# isinstance 判断对象是否是某类
# issubclass 判断某类是否另一个类的子类
# super 调用父类方法
# type 获知对象类型
print()
print(isinstance([1], list))
print(type([]))


# iter 返回迭代器
print()
it = iter(range(10))
print(it)

# len 返回字符串/可迭代对象/列表/元组等的长度
print()
print(len('ddddddd'))


# list 列表
# tuple 元组
# range
# next
a = 'abcdefg'
it = iter(a)
print(it.__next__)


# max 返回最大值
# min 返回最小值
print()
print(max(1, 2, 3, 4))
print(min(1, 2, 3, 4))
print(max(range(0, 100)))
print(min(range(0, 100)))


# memoryview
print()
a = memoryview(b'abc')
print(a[0])


# object
print()
a = object()
print(a.__doc__)


# open 打开文件


# property 负责把一个方法变成属性调用，广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
# 下面例子中，age 只读，birth 可读写
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

s = Student()
s.birth = 20
print()
print(s.birth)
print(s.age)


# repr 转化为供解释器读取的形式
# str  用于将值转化为适于人阅读的形式
print()
print(repr('hello'))
print(str('hello'))


# reversed  翻转序列
# sorted 排序
# slice 切片
rg = range(6)
for i in reversed(rg):
    print(i, end=' ')

r = [3, 4, 5, 1, 6, 2]
for i in sorted(r):
    print(i, end=' ')

print()
print(r[::-1])   #相当于 reversed
print(r[::2])    # 奇数序列，步长2
print(r[1:10])   #从下标 1 到10，10超过序列长度取到最后
print(r[1:])     #从下标 1 到最后，结果同上
print(r[1:-1])   # 取中间的数

