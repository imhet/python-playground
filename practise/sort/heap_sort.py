# -*- coding: utf-8 -*-
# ---------------------------------------
# 堆排序，采用二叉堆的数据结构来实现的，实质上还是一维数组。二叉堆是一个近似完全二叉树 。
#
# 时间 Ο(nlogn) 空间 O(1) 不稳定
#
# 二叉堆具有以下性质：
# 1. 父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
# 2. 每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。
#
# 步骤
# 1. 构造最大堆（Build_Max_Heap）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆
# 2. 排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了
# 3. 最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点
# ---------------------------------------


def heap_sort(array):
    n = len(array)
    first = int(n / 2 - 1)
    for start in range(first, -1, -1):
        max_heapify(array, start, n - 1)
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        max_heapify(array, 0, end - 1)
    return array


def max_heapify(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break
