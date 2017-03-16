# 列表推导式 variable = [out_exp for out_exp in input_list if out_exp ]

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = [x ** 2 for x in range(10)]
print(squared)

# 字典推导式 {v: k for k, v in some_dict.items()}

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    }

print(mcase_frequency)

# 集合推导式 跟列表推导式也是类似的。 唯一的区别在于它们使用大括号{}
squared = {x ** 2 for x in [1, 1, 2]}
print(squared)
