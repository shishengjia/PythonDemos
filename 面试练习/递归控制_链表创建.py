# coding:utf-8


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


def create_linked_list(values):
    """
    creats a linked list
    :param values: the data to create the linked list
    :return: head of the linked list 
    """
    """
    注意values[1:],如果values的长度为1，则返回[]，符合程序的要求
    """
    if len(values) == 0:
        return None
    first_node = Node(values[0])
    head_of_sublist = create_linked_list(values[1:])
    first_node.next_node = head_of_sublist
    return first_node


def reversed_linked_list(head):
    """
    reverse the linked list
    :param head: head of the linked list
    :return: the head of the reversed linked list  
    """
    # 如果head本身为空或者head的下一个节点为空，即只有本身自己一个节点，则返回自身
    if head is None or head.next_node is None:
        return head

    new_head = reversed_linked_list(head.next_node)
    head.next_node.next_node = head
    head.next_node = None
    return new_head


def print_nodes(head):
    while head:
        print(head.value)
        head = head.next_node

data = [1, 2, 3, 4, 5, 6]
head = create_linked_list(data)
print_nodes(head)
reversed_head = reversed_linked_list(head)
print_nodes(reversed_head)



