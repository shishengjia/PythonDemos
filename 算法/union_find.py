# coding: utf-8
from union_find_test_helper import UFTestHelper


class UnionFind:
    def __init__(self, n):
        self.data = []
        self.count = n
        # 初始化, 每一个data[i]指向自己, 没有合并的元素
        for i in range(n):
            self.data.append(i)

    def find(self, p):
        """
        返回元素的集合编号
        """
        return self.data[p]

    def is_connected(self, p, q):
        """
        判断两个元素是否属于一个集合
        O(1)
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        合并两个元素所属的集合
        O(n)
        """
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            return

        # 合并过程需要遍历一遍所有元素, 将两个元素的所属集合编号合并
        for i in range(self.count):
            if self.data[i] == q_id:
                self.data[i] = p_id


class UnionFind2:
    """
    定义根节点，self.data[i] = i ,即自己是自己的父亲
    """

    def __init__(self, n):
        self.data = []
        self.count = n

        # 初始的父亲都是自己
        for i in range(n):
            self.data.append(i)

    def find_parent(self, q):
        """
        寻找q元素所在集合的父亲
        """
        while q != self.data[q]:
            q = self.data[q]

        return q

    def find_all(self, q):
        """
        寻找 q 所在集合里的所有元素
        """
        q_parent = self.find_parent(q)

        for i in range(self.count):
            if self.data[i] == q_parent:
                print(i, end=' ')

    def is_connected(self, q, p):
        """
        是否属于一个集合，就看自己集合的父亲是否相等
        """
        return self.find_parent(q) == self.find_parent(p)

    def union(self, p, q):
        p_parent = self.find_parent(p)
        q_parent = self.find_parent(q)

        if p_parent == q_parent:
            return

        # 如果两个元素所在集合的父亲不是同一个，则将其中一个集合的父亲指向另一个集合的父亲，自己不再是父亲
        self.data[q_parent] = p_parent

    def print_data(self):
        for i in range(self.count):
            print(i, end=' ')

        print()

        for i in range(self.count):
            print(self.data[i], end=' ')


"""
基于 SIZE 的优化
在UnionFind2的 union 函数中， 两个元素所在集合的合并是随意的，则可能导致某一个集合的层数非常高，影响整体效率
所以为每个集合维护一个 size， 记录当前集合中元素的数量，在合并的时候总是小的集合的父亲去指向大的集合的父亲
当然这也不是绝对的（特殊情况下该优化不适用）
"""


class UnionFind3:
    """
    定义根节点，self.data[i] = i ,即自己是自己的父亲
    """

    def __init__(self, n):
        self.data = []
        self.count = n
        self.size = []

        # 初始的父亲都是自己
        for i in range(n):
            self.data.append(i)
            # 初始化每个集合只有一个元素
            self.size.append(1)

    def find_parent(self, q):
        """
        寻找q元素所在集合的父亲
        """
        while q != self.data[q]:
            q = self.data[q]

        return q

    def find_all(self, q):
        """
        寻找 q 所在集合里的所有元素
        """
        q_parent = self.find_parent(q)

        for i in range(self.count):
            if self.data[i] == q_parent:
                print(i, end=' ')

    def is_connected(self, q, p):
        """
        是否属于一个集合，就看自己集合的父亲是否相等
        """
        return self.find_parent(q) == self.find_parent(p)

    def union(self, p, q):
        p_parent = self.find_parent(p)
        q_parent = self.find_parent(q)

        if p_parent == q_parent:
            return

        # 谁的集合的元素少，就让该集合的父亲去指向元素多的集合的父亲，并更新相应的 size
        if self.size[p_parent] < self.size[q_parent]:
            self.data[p_parent] = q_parent
            self.size[q_parent] += self.size[p_parent]
        else:
            self.data[q_parent] = p_parent
            self.size[p_parent] += self.size[q_parent]

    def print_data(self):
        for i in range(self.count):
            print(i, end=' ')

        print()

        for i in range(self.count):
            print(self.data[i], end=' ')


"""
基于 RANK 的优化
集合A：层数很低，元素很多
集合B：层数很高，元素很少
将B集合归并到A集合的话，那么合并后的集合的层数将增加，但是如果是集合A归并到B集合的话，合并后集合的层数就不会增加（依然是B集合的层数）
如果两个集合的层数相等的话，那就无所谓了，最终合并后的层数 +1 就行了

所以每个集合可以维护一个 rank，记录自身的层数
"""


class UnionFind4:
    """
    定义根节点，self.data[i] = i ,即自己是自己的父亲
    """

    def __init__(self, n):
        self.data = []
        self.count = n
        self.rank = []

        # 初始的父亲都是自己
        for i in range(n):
            self.data.append(i)
            # 初始化每个集合的层数为 1
            self.rank.append(1)

    def find_parent(self, q):
        """
        寻找q元素所在集合的父亲
        """
        while q != self.data[q]:
            q = self.data[q]

        return q

    def find_all(self, q):
        """
        寻找 q 所在集合里的所有元素
        """
        q_parent = self.find_parent(q)

        for i in range(self.count):
            if self.data[i] == q_parent:
                print(i, end=' ')

    def is_connected(self, q, p):
        """
        是否属于一个集合，就看自己集合的父亲是否相等
        """
        return self.find_parent(q) == self.find_parent(p)

    def union(self, p, q):
        p_parent = self.find_parent(p)
        q_parent = self.find_parent(q)

        if p_parent == q_parent:
            return

        # 总是层数少的集合归并到层数高的集合中去，层数不变
        # 相等的话则无所谓，最终合并后的层数都会 +1
        if self.rank[q_parent] < self.rank[p_parent]:
            self.data[q_parent] = p_parent
        elif self.rank[p_parent] < self.rank[q_parent]:
            self.data[p_parent] = q_parent
        else:
            self.data[p_parent] = q_parent
            self.rank[q_parent] += 1


"""
上面，不管是针对 SIZE 的优化还是针对 RANK 的优化，都是针对 union 操作的优化，针对层数的优化
"""


"""
在上面 RANK 优化的基础上，进一步优化：路径压缩 （针对搜寻父亲的过程, 即 find_parent 函数）
1：递归调用 find_parent 函数，最终所有集合里的所有节点都会直接指向父亲，此时这个集合的层数只有 2
2：使元素的父亲为它父亲元素的父亲(向上跳跃，压缩了路径)，这样可以减少搜寻时间，而且最终集合的层数也会降低
    另外也不会出现跟索引有关的问题，因为最终的父亲节点始终指向自己

虽然第一种方法的层数更低，但是由于使用了递归，性能上不一定更快
"""


class UnionFind5:
    """
    定义根节点，self.data[i] = i ,即自己是自己的父亲
    """

    def __init__(self, n):
        self.data = []
        self.count = n
        self.rank = []

        # 初始的父亲都是自己
        for i in range(n):
            self.data.append(i)
            # 初始化每个集合的层数为 1
            self.rank.append(1)

    def find_parent(self, q):
        """
        寻找q元素所在集合的父亲
        """
        while q != self.data[q]:
            # 使 q 元素的父亲为它父亲元素的父亲(向上跳跃，压缩了路径)，这样可以减少搜寻时间，而且最终集合的层数也会降低
            # 另外也不会出现跟索引有关的问题，因为最终的父亲节点始终指向自己
            self.data[q] = self.data[self.data[q]]
            q = self.data[q]

        # 这里使用递归， self.find_parent(self.data[q])最终会返回父亲，这样父亲之外的所有元素都指向了父亲
        # 父亲的父亲就是自己，直接返回 self.data[q]即可
        # if q != self.data[q]:
        #     self.data[q] = self.find_parent(self.data[q])
        #
        # return self.data[q]
        return q

    def find_all(self, q):
        """
        寻找 q 所在集合里的所有元素
        """
        q_parent = self.find_parent(q)

        for i in range(self.count):
            if self.data[i] == q_parent:
                print(i, end=' ')

    def is_connected(self, q, p):
        """
        是否属于一个集合，就看自己集合的父亲是否相等
        """
        return self.find_parent(q) == self.find_parent(p)

    def union(self, p, q):
        p_parent = self.find_parent(p)
        q_parent = self.find_parent(q)

        if p_parent == q_parent:
            return

        # 总是层数少的集合归并到层数高的集合中去，层数不变
        # 相等的话则无所谓，最终合并后的层数都会 +1
        if self.rank[q_parent] < self.rank[p_parent]:
            self.data[q_parent] = p_parent
        elif self.rank[p_parent] < self.rank[q_parent]:
            self.data[p_parent] = q_parent
        else:
            self.data[p_parent] = q_parent
            self.rank[q_parent] += 1


uf_test = UFTestHelper(100000)
uf_test.test(UnionFind4)
print()
uf_test.test(UnionFind5)
