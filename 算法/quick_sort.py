# coding: utf-8
from sort_test_helper import TestHelper
import random
import time
import sys
"""
快速排序
双路快排
三路快排
"""


def partition(arr, l, r):
    # 当排序数组近乎有序的时候，每次选用第一个元素，将使时间复杂度成为O(n2)，所以应该随机选一个数，替换首元素，再进行排序
    random.seed(int(time.time()))
    n = random.randint(0, r-l) + l
    arr[n], arr[l] = arr[l], arr[n]
    # 指定首元素为用来比较的元素
    v = arr[l]
    # 初始化 j 为首元素的索引, 遍历过程中始终保持 j 为分界点，左边小于等于v， 右边大于v
    j = l
    # i 从 l+1 开始遍历
    for i in range(l+1, r+1):
        # 如果元素小于比较元素，则将该元素与 j+1 所在的元素交换位置， 并使 j 向后移一位
        if arr[i] < v:
            arr[i], arr[j+1] = arr[j+1], arr[i]
            j += 1

    # j 所在的元素与首元素交换， 并返回
    arr[l], arr[j] = arr[j], arr[l]
    return j


def __quick_sort(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)
    # 对分界点两边的数组继续进行
    __quick_sort(arr, l, p-1)
    __quick_sort(arr, p+1, r)


def quick_sort(arr, n):
    __quick_sort(arr, 0, n-1)


# 设置递归深度
# sys.setrecursionlimit(10000)
# t = TestHelper()
# arr = t.generate_nearly_ordered_arrar(100000, 10)
# arr_2 = t.generate_random_array(100000, 0, 10)
# t.test_sort('quick_sort', quick_sort, arr=arr, n=len(arr))
# t.test_sort('quick_sort', quick_sort, arr=arr_2, n=len(arr_2))


"""
在上面的partition，如果一个数组中重复的元素过多，会导致每次分组后两边的长度极度不平衡，会使该算法退化为O(n2)
需要重新写partition的逻辑，使用双路快排,确保每次分组后两边的元素个数相近
"""


def partition_2(arr, l, r):
    # 当排序数组近乎有序的时候，每次选用第一个元素，将使时间复杂度成为O(n2)，所以应该随机选一个数，替换首元素，再进行排序
    random.seed(int(time.time()))
    n = random.randint(0, r-l) + l
    arr[n], arr[l] = arr[l], arr[n]
    # 指定首元素为用来比较的元素
    v = arr[l]

    # 左索引 arr[l+1, i) 记录 <=v 的元素
    i = l + 1
    # 右索引 arr(j, r] 记录 >=v 的元素
    j = r
    while True:
        while i <= r and arr[i] < v:
            i += 1

        while j >= l+1 and arr[j] > v:
            j -= 1

        if i >= j:
            break

        # 此时两个游标都已经停止，arr[i]>=v, arr[j]<=v, 交换两个元素，在分别移动下标
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[j], arr[l] = arr[l], arr[j]
    return j


def __quick_sort_2(arr, l, r):
    if l >= r:
        return
    p = partition_2(arr, l, r)
    # 对分界点两边的数组继续进行
    __quick_sort_2(arr, l, p-1)
    __quick_sort_2(arr, p+1, r)


def quick_sort_2(arr, n):
    __quick_sort_2(arr, 0, n-1)


sys.setrecursionlimit(1000)
t = TestHelper()
arr_2 = t.generate_random_array(100000, 0, 10)
t.test_sort('quick_sort_2', quick_sort_2, arr=arr_2, n=len(arr_2))


"""
下面再次改进上面的算法，当数组中大量存在 ==v 的元素时，则可以将 这一部分单独隔离出来，不再参与排序，以再次提升性能
"""


def partition3_(arr, l, r):
    # 当排序数组近乎有序的时候，每次选用第一个元素，将使时间复杂度成为O(n2)，所以应该随机选一个数，替换首元素，再进行排序
    random.seed(int(time.time()))
    n = random.randint(0, r-l) + l
    arr[n], arr[l] = arr[l], arr[n]
    # 指定首元素为用来 比较的元素
    v = arr[l]

    """
    初始索引,此时
    arr[l+1, lt] < v
    arr[lt+1, i] == v
    arr[gt, r] > v
    """
    lt = l
    i = l + 1
    gt = r + 1

    while i < gt:
        if arr[i] < v:
            arr[lt+1], arr[i] = arr[i], arr[lt+1]
            lt += 1
            i += 1
        elif arr[i] > v:
            # 此时 i 位置上的元素为从后面刚换过来的，继续进行比较，不用进行 i +=1 的操作
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            gt -= 1
        else:  # arr[i] == v, 直接 i += 1
            i += 1
    """
    交换位置后,
    arr[l, lt-1] < v
    arr[lt, i] == v
    arr[gt, r] > v   
    """
    arr[l], arr[lt] = arr[lt], arr[l]

    return lt, gt


def __quick_sort_3(arr, l, r):
    if l >= r:
        return

    lt, gt = partition3_(arr, l, r)
    __quick_sort_3(arr, l, lt-1)
    __quick_sort_3(arr, gt, r)


def quick_sort_3(arr, n):
    __quick_sort(arr, 0, n-1)


t = TestHelper()
arr_3 = t.generate_random_array(100000, 0, 10)
t.test_sort('quick_sort_3', quick_sort_2, arr=arr_3, n=len(arr_3))

