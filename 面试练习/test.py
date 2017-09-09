# coding:utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


def create_linked_list(list):

    if len(list) == 0:
        return None

    head = Node(list[0])
    head.next_node = create_linked_list(list[1:])
    return head


def reversed_linked_list(head):
    """
    递归
    :param head: 
    :return: 
    """
    if head is None or head.next_node is None:
        return head

    new_head = reversed_linked_list(head.next_node)
    head.next_node.next_node = head
    head.next_node = None
    return new_head


def reversed_linked_list_2(head):
    """
    非递归
    :param head: 
    :return: 
    """
    p = head
    q = head.next_node
    head.next_node = None
    while q:
        r = q.next_node
        q.next_node = p
        p = q
        q = r
    return p


def mprint(head):
    while head:
        print(head.value, end=' ')
        head = head.next_node


my_list = create_linked_list([1, 2, 3, 4, 5])
mprint(my_list)

print('\n')

new_list = reversed_linked_list_2(my_list)
mprint(new_list)