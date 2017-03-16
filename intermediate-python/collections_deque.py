# deque提供了一个双端队列，你可以从头/尾两端添加或删除元素

from collections import deque

d = deque([1, 2, 3, 4, 5])

# 从任一端扩展这个队列中的数据
d.extendleft([0])
d.extend([6, 7, 8])
print(d)

# 增加元素
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])
print(d)

# 从两端取出(pop)数据
d.popleft()
d.pop()
print(d)
