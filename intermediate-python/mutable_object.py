# 可变对象


def add_to1(num, target=[]):
    target.append(num)
    return target


print(add_to1(1))

print(add_to1(2))

print(add_to1(3))


def add_to2(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


print(add_to2(1))

print(add_to2(2))

print(add_to2(3))
