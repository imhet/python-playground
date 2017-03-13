# -*- coding: utf-8 -*-
# ---------------------------------------
# 快速排序，采用了分治法的思想
#
# 时间 Ο(nlogn) 空间 O(logn) ~ O(n)  不稳定
#
# 1. 从数列中挑出一个元素作为基准数
# 2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边
# 3. 再对左右区间递归执行第二步，直至各区间只有一个数
# ---------------------------------------


def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)


def qsort(array, left, right):
    if left >= right:
        return array

    key = array[left]
    lp = left
    rp = right
    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1
        while array[lp] <= key and lp < rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]

    array[left], array[lp] = array[lp], array[left]
    qsort(array, left, lp - 1)
    qsort(array, rp + 1, right)

    return array
