# * 表达式
#first和last分别是第一和最后一个元素，middle位中间所有元素的列表
first, *middle, last = [34, 56, 78, 66, 100]
print(first, middle, last)

#下面同理

*first, others = [34, 56, 78, 66, 100]
print(first, others)

others, *last = [34, 56, 78, 66, 100]
print(others, last)

records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]

# 迭代一个变长的元祖序列

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    print(tag, args)
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)

# 引用场景,结合字符串的处理操作
line = 'shishengjia:*: 2 -2:2:1:Unprivileged User:/var/empty:/usr/bin/false'
name, *fields, homedir, sh = line.split(':')
print(name, homedir, sh)
