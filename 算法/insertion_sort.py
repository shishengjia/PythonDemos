# coding:utf8


def insertion_sort(arr):
    # 从第一个元素开始，第零个元素不用管
    for i in range(1, len(arr)):
        # 需要插入的元素
        guard = arr[i]
        # 存放需要插入的位置
        index = 0
        for j in reversed(range(1, i+1)):
            # 插入元素小的话，则将当前位置元素的值替换成前一个元素的值
            if guard < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                # 记录需要插入的位置，并停止此次循环
                index = j
                break
        arr[index] = guard
    return arr


print(insertion_sort([1, 3, 2, 44, 11, 3]))
