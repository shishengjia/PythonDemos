# coding: utf-8
import time
import random


class MaxHeap:
    """
    最大堆,标号从1开始
    i 号元素
    parent: i//2
    left children: 2*i
    right children: 2*i+1
    """
    def __init__(self):
        # 不使用 零号 元素，设为None，之后动态添加元素
        self.__data = [None]
        self.__count = 0

    def __len__(self):
        """
        返回堆的大小
        """
        return self.__count

    def is_empty(self):
        """
        堆是否为空
        """
        return self.__count == 0

    def __shift_up(self, k):
        """
        将新插入的元素调整到合适的位置，维持最大堆的定义
        :param k: 元素序号
        """
        # 保存要插入的元素
        v = self.__data[k]
        while k > 1 and self.__data[k//2] < v:
            self.__data[k] = self.__data[k//2]
            k = k // 2
        self.__data[k] = v

    def __shift_down(self, k):
        """
        将新的根节点移动到合适的位置，维持最大堆的定义
        """
        # 保存要比较的元素
        v = self.__data[k]
        # 如果有左孩子的话
        while k*2 <= self.__count:
            j = k*2
            # 通过比较使 j 指向两个孩子中大的一个
            if j + 1 <= self.__count and self.__data[j+1] > self.__data[j]:
                j += 1
            # j 指向的节点（两个孩子中最大的一个）如果小于v，则符合最大堆得定义，停止循环
            if v > self.__data[j]:
                break
            # 否则，将 j 指向的孩子节点的值赋给现在的k所在的元素，并把j的值赋给 k
            self.__data[k] = self.__data[j]
            k = j
        # 此时 k 已经在合适的位置
        self.__data[k] = v

    def insert(self, item):
        """
        插入新的元素
        """
        self.__data.append(item)
        self.__count += 1
        self.__shift_up(self.__count)

    def remove(self):
        """
        移除根节点，即最大的元素（优先级最大）
        """
        # 将最后一个元素填补到根节点，计数 -1
        print(self.__data[1], end=' ')
        self.__data[self.__count], self.__data[1] = self.__data[1], self.__data[self.__count]
        self.__count -= 1
        # 然后调整新的根节点的位置,再维持最大堆的定义
        self.__shift_down(1)

    def print_data(self):
        for i in range(1, self.__count+1):
            print(self.__data[i], end=' ')


heap = MaxHeap()
random.seed(int(time.time()))
for i in range(15):
    j = random.randint(1, 100)
    heap.insert(j)
print()
heap.print_data()
print()
for i in range(1, len(heap)+1):
    heap.remove()

