# coding:utf-8


def combination(arr, n, arr_selected=None):

    if arr_selected is None:
        arr_selected = []

    if n == 0:
        for i in arr_selected:
            print(i, end=' ')
        print()
        return

    if len(arr) == 0:
        return

    arr_selected.append(arr[0])
    combination(arr[1:], n-1, arr_selected)

    # 注意递归返回的顺序，应该弹出最后一个
    arr_selected.pop(len(arr_selected) - 1)
    combination(arr[1:], n, arr_selected)

combination([1, 2, 3, 4], 2)
print('-------------------')
combination([], 2)
print('-------------------')
combination([1, 2, 3, 4], 0)
print('-------------------')
combination([1, 2, 3, 4, 5], 3)



