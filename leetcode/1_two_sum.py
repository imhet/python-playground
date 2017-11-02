# 需找出一个列表中是否有两个数的和为一个给定的数，并返回这两个数的下标
# 需要用到python里面的字典（相当于hash表），判断第i个数前面是否有一个数的值为target - num[i]


def twoSum1(num, target):
    tmp = {}
    for i in range(len(num)):
        if target - num[i] in tmp:
            return (tmp[target - num[i]], i)
        else:
            tmp[num[i]] = i


def twoSum2(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[j] == target - num[i]:
                return (i, j)


print(twoSum1([2, 7, 11, 10, 1, 15], 3))
print(twoSum2([2, 7, 11, 10, 1, 15], 3))
