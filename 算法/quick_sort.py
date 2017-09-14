# coding: utf-8
"""
手推演算一遍可以看得更明白
"""


def partition(arr, l, r):
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


list = [4, 1, 4, 5, 8, 3, 6]
quick_sort(list, len(list))
print(list)