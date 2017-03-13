# -*- coding: utf-8 -*-
# ---------------------------------------
# 希尔排序，也称递减增量排序算法，实质是分组插入排序。由 Donald Shell 于1959年提出。希尔排序是非稳定排序算法。
#
# 时间 Ο(nlogn) ~ Ο(n*n) 空间 O(1)  不稳定

# 基本原理：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列即排序完成
# ---------------------------------------


def shell_sort(array):
    n = len(array)
    gap = round(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while (j >= gap and array[j - gap] > temp):
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap = round(gap / 2)
    return array
