# 检查列表中是否包含重复的元素

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 两个集合的交集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(valid.intersection(input_set))

# 差集(difference)找出无效的数据，相当于用一个集合减去另一个集合的数据
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
print(valid.difference(input_set))
