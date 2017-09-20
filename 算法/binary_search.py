# coding:utf-8
from sort_test_helper import TestHelper
# 二分查找


def binary_search(arr, n, item):
    """
    非递归版本
    :param arr: 数组
    :param n: 数组长度
    :param item: 查找元素
    :return: 元素索引
    """
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r-l) // 2
        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binary_search_2(arr, l, r, item):
    """
    递归版本
    """
    if l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search_2(arr, l, mid - 1, item)
        else:
            return binary_search_2(arr, mid + 1, r, item)
    else:
        return -1


def floor(arr, n, item):
    """
    二分查找法, 在有序数组arr中, 查找item
    如果找到item, 返回第一个item相应的索引index
    如果没有找到item, 返回比item小的最大值相应的索引, 如果这个最大值有多个, 返回最大索引
    """
    # 如果这个item比整个数组的最小元素值还要小, 则不存在这个item的floor值, 返回-1
    if item < arr[0]:
        return -1

    l = 0
    r = n-1
    while l < r:
        # 为了防止死循环，采用向上取整
        mid = l + (r-l+1) // 2
        if arr[mid] >= item:
            r = mid - 1
        else:
            l = mid

    assert l == r

    # 如果该索引+1就是item本身, 该索引+1即为返回值
    if l + 1 < n and arr[l+1] == item:
        return l + 1

    # 否则返回l，即比item小的最大值的索引
    return l


def ceil(arr, n, item):
    """
    二分查找法, 在有序数组arr中, 查找item
    如果找到item, 返回最后一个item相应的索引index
    如果没有找到item, 返回比item大的最小值相应的索引, 如果这个最小值有多个, 返回最小的索引
    """
    # 如果这个item比整个数组的最大元素值还要大, 则不存在这个item的ceil值, 返回-1
    if item > arr[n-1]:
        return -1

    l = 0
    r = n-1
    while l < r:
        # 采用向下取整即可避免死循环
        mid = l + (r-l)//2
        if arr[mid] <= item:
            l = mid + 1
        else:
            r = mid
    assert l == r

    # 如果该索引-1就是item本身, 该索引-1即为返回值
    if r - 1 >= 0 and arr[r-1] == item:
        return r - 1

    return r


t = TestHelper()
arr = [3, 11, 11, 23, 45, 66, 77]
print(ceil(arr, len(arr), 4))


