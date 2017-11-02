# 一行代码打印九九乘法表

print('\n'.join([' '.join(['%s*%s=%s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
