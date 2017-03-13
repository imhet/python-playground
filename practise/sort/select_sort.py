# -*- coding: utf-8 -*-
# ---------------------------------------
# 选择排序
#
# 时间 Ο(n*n) 空间 O(1)  不稳定
#
# 1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
# 2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
# 3. 以此类推，直到所有元素均排序完毕
# ---------------------------------------


def select_sort(array):
    n = len(array)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array
