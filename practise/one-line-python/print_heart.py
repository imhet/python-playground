# 一行 代码打印心形

print('\n'.join([''.join([('*******'[(x-y) % 7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ')for x in range(-30, 30)])for y in range(15, -15, -1)]))

# 曼德博集合

print('\n'.join([''.join(['*'if abs((lambda a:lambda z, c , n:a(a, z, c, n))(lambda s, z, c, n:z if n == 0 else s(s, z*z + c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else' 'for x in range(-80, 20)])for y in range(-20, 20)]))

# 一行代码计算出1-1000之间的素数
print(*(i for i in range(2, 1000) if all(tuple(i%j for j in range(2, int(i**.5))))))
