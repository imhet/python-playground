# lambda表达式说明 ： https://www.zhihu.com/question/20125256

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))

for i in squared:
    print(i)


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(10):
    value = map(lambda x: x(i), funcs)
    print(list(value))
