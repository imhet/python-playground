# -*- coding: utf-8 -*-
# ---------------------------------------
# 插入排序，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
#
# 时间 Ο(n*n) 空间 O(1) 稳定
#
# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置后
# 6. 重复步骤2~5
# ---------------------------------------


def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        if array[i] < array[i - 1]:
            temp = array[i]
            index = i
            for j in range(i - 1, -1, -1):
                if array[j] > temp:
                    array[j + 1] = array[j]
                    index = j
                else:
                    break
            array[index] = temp
    return array
