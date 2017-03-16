# 枚举(enumerate)是Python内置函数
# 它允许我们遍历数据并自动计数
# 下面这个可选参数 1 允许我们定制从哪个数字开始枚举

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 2):
    print(c, value)

# 还可以用来创建包含索引的元组列表
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
