class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


def print_list(head):
    while head:
        print(head.value, end='')
        head = head.next_node


def create_linked_list(strs):
    lower_pre = lower_head = None
    upper_pre = upper_head = None
    lower_head_exists = False
    upper_head_exists = False
    for x in strs:
        if not lower_head_exists and x.islower():
            lower_pre = lower_head = Node(x)
            lower_head_exists = True
            continue
        if not upper_head and x.isupper():
            upper_pre = upper_head = Node(x)
            upper_head_exists = True
            continue

        if x.islower():
            node = Node(x)
            lower_pre.next_node = node
            lower_pre = node

        if x.isupper():
            node = Node(x)
            upper_pre.next_node = node
            upper_pre = node
    lower_pre.next_node = upper_head
    return lower_head

n = input()
str = input()
lower_head = create_linked_list(str)
print_list(lower_head)







