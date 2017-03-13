# -*- coding: utf-8 -*-
# ---------------------------------------
# 归并排序，先递归分解数组，再合并数组
#
# Ο(nlogn) 空间 O(n) 稳定
#
# 1. 合并两有序数组：比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可
# 2. 递归分解：将数组分解成left和right，如果这两个数组内部数据是有序的，那么将这两数组合并。如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时该小组内部已有序。
# ---------------------------------------


def merge_sort(array):
    if len(array) <= 1:
        return array
    num = int(len(array) / 2)
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
