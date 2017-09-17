# coding:utf-8
from sort_test_helper import TestHelper


def __merge(arr, l, mid, r):
    """
    归并排序核心思路
    :param arr: 整个数组 
    :param l: 左半部分起始索引
    :param mid: 中间值
    :param r: 右半部分起始索引
    """
    # 构造一个相同的数组,注意开闭区间
    temp = arr[l:r+1]

    # 左半边起始索引
    i = l
    # 右半边起始索引
    j = mid + 1

    # 注意偏移量l，使用temp数组操作时需要减去,防止越界
    for k in range(l, r+1):
        # 左半边已经遍历完,添加右半边的元素即可
        if i > mid:
            arr[k] = temp[j-l]
            j += 1
        # 右半边已经遍历完,添加左半边的元素即可
        elif j > r:
            arr[k] = temp[i-l]
            i += 1

        # 左半边的元素小于右半边的元素，则使用左半边的元素进行赋值
        elif temp[i-l] < temp[j-l]:
            arr[k] = temp[i-l]
            i += 1
        else:
            arr[k] = temp[j-l]
            j += 1


def __merge_sort(arr, l, r):
    """
    一个可以优化的方案是，当数组近乎有序的时候，可以使用插入排序，因为插入排序在数组近乎有序的情况下时间复杂度只比O(n)
    if (r - l) < 15:
        insertionsort(arr, l, r)
    注意这里需要写一个特殊的插入排序，指定起始和结束位置
    """
    if l >= r:
        return

    mid = l + (r - l) // 2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid+1, r)
    if arr[mid] > arr[mid+1]:
        __merge(arr, l, mid, r)


def merge_sort(arr, n):
    # 注意这里使用的列表的长度减1，即最后一个元素的下表
    __merge_sort(arr, 0, n-1)


t = TestHelper()
arr = t.generate_random_array(100000, 100, 1000)
t.test_sort('test', merge_sort, arr=arr, n=len(arr))

