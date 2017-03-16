# 你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。进入到你要共享文件的目录下并在命令行中运行下面的代码
# python -m SimpleHTTPServer


# 漂亮的打印
from pprint import pprint
import itertools

my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)

# 快速漂亮的从文件打印出json数据
# cat file.json | python -m json.tool

# 可能在定位你的脚本中的性能瓶颈时，会非常奏效
# python -m cProfile my_script.py


# CSV 转 json
# python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"


# 列表压平

a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))
