import random
import time


class TestHelper:
    def generate_random_array(self, n, rangeL, rangeR):
        """
        :param n: 元素个数
        :param rangeL: 左边界
        :param rangeR: 右边界
        :return: 随机数组
        """
        assert rangeL <= rangeR

        arr = [None for _ in range(n)]
        # 设置随机数种子，以时间作为种子，确保每次不一样
        random.seed(int(time.time()))
        for i in range(n):
            arr[i] = random.randint(rangeL, rangeR) % (rangeR - rangeL + 1) + rangeL

        return arr

    def generate_nearly_ordered_arrar(self, n, swap_time):
        """
        :param n: 范围
        :param swap_time: 随机交换次数
        :return: 一个近乎有序的数组
        """
        random.seed(int(time.time()))
        arr = [x for x in range(n)]
        for i in range(swap_time):
            position_a = random.randint(0, n-1)
            position_b = random.randint(0, n-1)
            arr[position_a], arr[position_b] = arr[position_b], arr[position_a]
        return arr

    def test_sort(self, sort_name, sort_def, **kwargs):
        """
        :param sort_name: 排序函数名称
        :param sort_def: 排序函数
        :param kwargs: 额外参数，包括 数组 arr 和 元素个数 n
        :return: 有序的数组
        """
        arr = kwargs.get('arr')
        n = kwargs.get('n')
        start_time = time.time()
        sort_def(arr, n)
        end_time = time.time()
        print('{:.6f} s'.format(end_time - start_time))

    def print_array(self, arr):
        for x in arr:
            print(x, end=' ')
        print()

