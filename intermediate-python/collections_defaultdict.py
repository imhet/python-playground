# 与dict类型不同，你不需要检查key是否存在


from collections import defaultdict
import json

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# 当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常。 defaultdict允许我们用一个聪明的方式绕过这个问题

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

print(json.dumps(some_dict))
