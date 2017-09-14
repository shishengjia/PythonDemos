# coding: utf-8

"""
有四个数a,b,A,B
对a,b同时进行 +1 或者 *2 的操作
需要经过几次操作才能使 a==A and b == B

输入：100 1000 202 2002
输出：2
"""


def calculate(x, y):
    count = 0
    while x != y and x > y:
        if x % 2 == 0:
            x = x / 2
            count += 1
        else:
            x -= 1
            count += 1
    if x == y:
        return count
    else:
        return -1


a = int(raw_input())
b = int(raw_input())
A = int(raw_input())
B = int(raw_input())

count_a = 0
count_b = 0

if a == A and b == B:
    print count_a
elif a > A or b > B:
    print -1
elif (a != A and b == B) or (a == A and b != B):
    print -1
else:
    count_a = calculate(A, a)
    count_b = calculate(B, b)
    if count_a == count_b:
        print count_a
    else:
        print -1

