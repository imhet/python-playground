# namedtuples 把元组变成一个针对简单任务的容器,你不必使用整数索引来访问一个namedtuples的数据。你可以像字典(dict)一样访问namedtuples，但namedtuples是不可变的
# 一个命名元组(namedtuple)有两个必需的参数。它们是元组名称和字段名称。
# 我们这里的元组名称是Animal，字段名称是'name'，'age'和'type'。namedtuple让你的元组变得自文档了

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
print(perry.name)

# 要记住它是一个元组，属性值在namedtuple中是不可变的
# perry.age = 42

print(perry[0])

# 将一个命名元组转换为字典
print(perry._asdict())
