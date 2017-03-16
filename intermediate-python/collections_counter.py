from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

# Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色

favs = Counter(name for name, colour in colours)
print(favs)

# 利用它统计一个文件

with open('map.py', 'rb') as f:
    line_count = Counter(f)
print(line_count)
