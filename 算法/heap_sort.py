# coding: utf-8

from heap import MaxHeap
from sort_test_helper import TestHelper


def heap_sort(arr, n):
    """
    使用已经实现的最大堆来实现排序
    """
    heap = MaxHeap()
    for i in range(n):
        heap.insert(arr[i])

    for j in reversed(range(n)):
        arr[j] = heap.remove()


def heap_sort_2(arr, n):
    heap = MaxHeap()
    heap.heapify(arr)

    for j in reversed(range(n)):
        arr[j] = heap.remove()


t = TestHelper()
arr = t.generate_random_array(100000, 100, 1000)
arr_2 = arr[:]
t.test_sort('heap_sort', heap_sort, arr=arr, n=len(arr))
t.test_sort('heap_sort_2', heap_sort_2, arr=arr_2, n=len(arr_2))


"""
原地堆排序—-进一步提升排序性能
主要思想：
    对于第一遍已经建好的堆，首元素arr[0]即为最大的元素，此时将首元素于最后一个元素arr[n]交换，那么最大的元素就已经就位了，
    针对剩余的元素arr[0, n-1]，只需要将arr[0]移动到合适的位置，使剩下的数组重新符合最大堆的定义即可
    然后重复上面的过程，这样就在不开辟新空间的情况下对数组完成了排序,提升了效率
    
    需要注意的是，此时元素节下标从0开始，第一个非叶子节点: (n-1)//2
    针对索引为 i 的元素：
        左孩子: i*2+1
        右孩子: i*2+2
"""


def shift_down(arr, n, k):
    """
    将新的根节点移动到合适的位置，维持最大堆的定义
    注意这里arr的下标从零开始
    """
    # 保存要比较的元素
    v = arr[k]
    # 如果有左孩子的话
    while k * 2 + 1 < n:
        j = k * 2 + 1
        # 通过比较使 j 指向两个孩子中大的一个
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        # j 指向的节点（两个孩子中最大的一个）如果小于v，则符合最大堆得定义，停止循环
        if v >= arr[j]:
            break
        # 否则，将 j 指向的孩子节点的值赋给现在的k所在的元素，并把j的值赋给 k
        arr[k] = arr[j]
        k = j
    # 此时 k 已经在合适的位置
    arr[k] = v


def heap_sort_3(arr, n):
    # 第一遍，从第一个非叶子节点开始依次调用 shift_down ，使整个数组符合最大堆的定义
    for i in reversed(range((n-1)//2+1)):
        shift_down(arr, n, i)

    # 每一次将最大的首元素和末尾元素交换后，只需调整零号元素的位置，使剩下的元素符合最大堆的定义
    for i in reversed(range(n)):
        arr[i], arr[0] = arr[0], arr[i]
        # 剩余 i 个元素，对索引为O的元素进行 shift_down 操作
        shift_down(arr, i, 0)
    return arr


arr_3 = arr[:]
t.test_sort('heap_sort_3', heap_sort_3, arr=arr_3, n=len(arr_3))




