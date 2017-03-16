# 三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断，在Python 2.4以上才有了三元操作
is_fat = True
state = "fat" if is_fat else "not fat"
print(state)

# 这种写法容易引起误解，少用
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
