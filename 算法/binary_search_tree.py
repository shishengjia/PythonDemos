# coding: utf-8
import re
from queue import Queue


class Node:
    """
    二分搜索树节点,包括 键 和 值，以及左右孩子
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_node = None
        self.right_node = None


class BST:
    """
    二叉搜索树
    """
    def __init__(self):
        # 根节点
        self.root = None
        # 节点数量
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        """
        二叉树是否为空
        """
        return self.count == 0

    def __insert(self, node, key, value):

        if node is None:
            # 如果为空,说明key还不存在,则创建新节点,并返回
            self.count += 1
            return Node(key, value)

        if node.key == key:  # key相等，则更新value
            node.value = value
        elif key < node.key:  # key小的话， 则往左子树方向走
            node.left_node = self.__insert(node.left_node, key, value)
        else:
            node.right_node = self.__insert(node.right_node, key, value)

        # 最终总是返回整棵树的根节点
        return node

    def insert(self, key, value):
        """
        插入新元素
        在比较元素的时候，以元素的 key 为比较依据
        """
        self.root = self.__insert(self.root, key, value)

    def __contain(self, node, key):

        # node为None，说明不穿在该节点
        if node is None:
            return False

        if node.key == key:
            return True
        elif key < node.key:  # key小于该节点的key，则往左子树继续寻找
            return self.__contain(node.left_node, key)
        else:
            return self.__contain(node.right_node, key)

    def contain(self, key):
        """
        查找是否包含指定元素
        """
        return self.__contain(self.root, key)

    def __search(self, node, key):
        # 查找不到返回空
        if node is None:
            return None

        if node.key == key:
            return node
        elif key < node.key:  # key小于该节点的key，则往左子树继续搜寻
            return self.__search(node.left_node, key)
        else:
            return self.__search(node.right_node, key)

    def search(self, key):
        """
        搜索指定元素并返回
        """
        return self.__search(self.root, key)

    def pre_order_traversal(self, root):
        """
        前序遍历
        """
        if root is not None:
            print(root.key, end=' ')
            self.pre_order_traversal(root.left_node)
            self.pre_order_traversal(root.right_node)

    def in_order_traversal(self, root):
        """
        中序遍历
        """
        if root is not None:
            self.in_order_traversal(root.left_node)
            print(root.key, end=' ')
            self.in_order_traversal(root.right_node)

    def post_order_traversal(self, root):
        """
        后序遍历
        """
        if root is not None:
            self.post_order_traversal(root.left_node)
            self.post_order_traversal(root.right_node)
            print(root.key, end=' ')

    def level_order_traversal(self, root):
        """
        层序遍历
        """
        queue = Queue()
        # 根节点入队
        if root is not None:
            queue.put(root)

        while not queue.empty():
            # 抛出结点并输出 key
            node = queue.get()
            print(node.key, end=' ')

            # 如果左孩子不为空，左孩子入队
            if node.left_node is not None:
                queue.put(node.left_node)

            # 如果右孩子不为空，右孩子入队
            if node.right_node is not None:
                queue.put(node.right_node)

    def __mini_node(self, node):
        if node.left_node is None:
            return node

        return self.__mini_node(node.left_node)

    def mini_node(self):
        """
        找到key最小的node
        """
        mini_node = self.__mini_node(self.root)
        return mini_node

    def __remove_min_node(self, node):
        # 如果左孩子为空，直接返回右孩子即可
        if node.left_node is None:
            self.count -= 1
            return node.right_node

        # 再在以node 的左孩子为根节点的子树中寻找
        node.left_node = self.__remove_min_node(node.left_node)

        # 最终返回根节点
        return node

    def remove_min_node(self):
        """
        删除 key 最小的元素, 并返回
        """
        if self.root:
            self.root = self.__remove_min_node(self.root)

    def __remove_node(self, node, key):
        if node is None:
            return None

        # 如果 key 小于当前节点的key的话，则继续在左子树寻找
        if key < node.key:
            node.left_node = self.__remove_node(node.left_node, key)
            return node
        # 如果 key 大于当前节点的key的话， 则继续在右子树寻找
        elif key > node.key:
            node.right_node = self.__remove_node(node.right_node, key)
            return node
        else:
            # 此时已经找到需要删除的节点

            # 如果该节点的左孩子为空的话，直接返回该节点的右孩子即可(两个孩子都为空的话也适用)
            if node.left_node is Node:
                self.count -= 1
                return node.right_node

            # 如果该节点的右孩子为空的话，直接返回该节点的左孩子即可
            if node.right_node is Node:
                self.count -= 1
                return node.left_node

            # 如果该节点左右孩子都存在的话

            # 找到该节点的右子树中的key最小的节点，使他成为继任节点，代替当前的节点(这样能够保证现在该节点的key大于所有
            # 左子树里的节点的key，小于所有右子树的节点里的key,继续维持二叉搜索树的性质)
            # 当然还有另外一种实现，将左子树中key最大的节点当做继任节点也是可以的
            successor_node = self.__mini_node(node.right_node)

            # 继任节点的右孩子则为右子树删除最小节点后返回的节点(即根节点)
            successor_node.right_node = self.__remove_min_node(node.right_node)

            # 继任节点的左孩子当然是上一任节点(即node)的左孩子
            successor_node.left_node = node.left_node

            # 最终返回继任节点
            return successor_node

    def remove_node(self, key):
        """
        删除一个节点
        """
        self.root = self.__remove_node(self.root, key)


# bst = BST()
# pat = re.compile('\w+')
#
# with open('bible.txt') as f:
#     for x in pat.findall(f.read()):
#         if bst.contain(x):
#             bst.search(x).value += 1
#         else:
#             bst.insert(x, 1)
#     print(bst.search('God').value)
bst = BST()
bst.insert(50, 123)
bst.insert(10, 123)
bst.insert(80, 123)
bst.insert(60, 123)
bst.insert(55, 123)
bst.insert(70, 123)
bst.insert(65, 123)
bst.insert(77, 123)
bst.insert(160, 123)
bst.level_order_traversal(bst.root)
print(bst.count)
bst.remove_node(60)
print()
bst.level_order_traversal(bst.root)
print(bst.count)
