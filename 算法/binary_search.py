# coding:utf-8

# 二分查找


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return mid
    return None

my_list = [1, 3, 5, 7, 9, 11]
print(binary_search(my_list, 9))