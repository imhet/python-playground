# yield 场景: 你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。
# 参考 https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibon(100):
    print(i)

# my_string 对象不是一个迭代器，它是一个可迭代对象。这意味着它支持迭代，但我们不能直接对其进行迭代操作，需要用到内置函数 iter
my_string = "hello world"
my_iter = iter(my_string)

for i in my_iter:
    print(i)
