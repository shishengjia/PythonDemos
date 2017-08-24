# coding:utf-8

# 选择排序


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(0, len(arr)):
        index = find_smallest(arr)
        new_arr.append(arr.pop(index))
    return new_arr


# print(selection_sort([1, 11, 3, 5, 22, 77]))
