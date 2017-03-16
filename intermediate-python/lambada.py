# lambda 参数:操作(参数)

add = lambda x, y: x + y
print(add(3, 5))

# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

# 列表并行排序
list1 = [1, 5, 3]
list2 = [2, 4, 6]
data = zip(list1, list2)
sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)
