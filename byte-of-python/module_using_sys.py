import sys
import os
from math import sqrt

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 获取当前文件的路径
print(os.getcwd())

print("Square root of 16 is", sqrt(16))
