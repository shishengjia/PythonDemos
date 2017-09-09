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


def create_linked_list_2(values):
    """
    非递归
    creats a linked list
    :param values: the data to create the linked list
    :return: head of the linked list 
    """
    """
    注意values[1:],如果values的长度为1，则返回[]，符合程序的要求
    """
    head = prev_node = Node(values[0])
    for i in range(1, len(values)):
        node = Node(values[i])
        prev_node.next_node = node
        prev_node = node
    return head


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
    # head节点的下一个节点指向head自身，反转
    head.next_node.next_node = head
    head.next_node = None
    return new_head


def reversed_linked_list_2(head):
    """
    非递归
    :param head: 
    :return: 
    """
    new_head = None
    current_head = head
    while current_head:
        temp = current_head.next_node
        current_head.next_node = new_head
        new_head = current_head
        current_head = temp
    return new_head


def delete_node(value, head):

    while head and head.value == value:
        head = head.next_node

    if head is None:
        return None

    prev_node = head

    while prev_node.next_node:
        if prev_node.next_node.value == value:
            prev_node.next_node = prev_node.next_node.next_node
        else:
            prev_node = prev_node.next_node

    return head


def print_nodes(head):
    while head:
        print(head.value, end=' ')
        head = head.next_node
    print()

data = [5, 5, 1, 2, 2]
head = create_linked_list_2(data)
print_nodes(head)
# reversed_head = reversed_linked_list_2(head)
# print_nodes(reversed_head)
head = delete_node(11, head)
print_nodes(head)


