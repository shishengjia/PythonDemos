# coding:utf-8

# 选择排序


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr


print(selection_sort([11, 6, 11, 5, 7, 66]))
