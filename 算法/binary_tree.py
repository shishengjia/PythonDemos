# coding:utf-8


class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


def create_tree(pre_order, in_order):
    """
    :param pre_order: 前序遍历 
    :param in_order: 中序遍历
    :return: 根节点
    """
    if len(pre_order) == 0:
        return None

    # root node
    root = Node(pre_order[0])

    # the index of root in in_order
    # equal to the length of the left sub_tree
    root_index = in_order.index(root.value)

    # create the left sub_tree
    root.left_node = create_tree(pre_order[1:1+root_index], in_order[:root_index])

    # create the right sub_tree
    root.right_node = create_tree(pre_order[root_index+1:], in_order[root_index+1:])

    return root


def pre_order(root):
    """
    前序遍历
    """
    if root is None:
        return
    print(root.value, end='')
    pre_order(root.left_node)
    pre_order(root.right_node)


def in_order(root):
    """
    中序遍历
    """
    if root is None:
        return
    in_order(root.left_node)
    print(root.value, end='')
    in_order(root.right_node)


def post_order(root):
    """
    后序遍历
    """
    if root is None:
        return

    post_order(root.left_node)
    post_order(root.right_node)
    print(root.value, end='')


root = create_tree('ABDEGCF', 'DBGEACF')
root_2 = create_tree('a', 'a')
post_order(root)
print()
post_order(root_2)




