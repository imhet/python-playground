# 一行代码排序字符串

print("".join((lambda x: (x.sort(), x)[1])(list('kjihgfedcba123'))))
