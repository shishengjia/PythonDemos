# coding: utf-8
import random
import time


class UFTestHelper:
    def __init__(self, n):
        self.n = n

    def test(self, UF):
        random.seed(int(time.time()))

        uf = UF(self.n)

        start_time = time.time()

        # 进行n次操作, 每次随机选择两个元素进行合并操作
        for i in range(self.n):
            a = random.randint(0, self.n - 1)
            b = random.randint(0, self.n - 1)
            uf.union(a, b)

        # 查操作
        for i in range(self.n):
            a = random.randint(0, self.n - 1)
            b = random.randint(0, self.n - 1)
            uf.is_connected(a, b)

        end_time = time.time()
        print('{:.6f}'.format(end_time - start_time))

