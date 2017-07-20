"""
使用next()方法
StopIteration异常是用来通知迭代结束的
"""
with open('../records.txt') as f:
    try:
        while True:
            line = next(f)
            print(line)
    except StopIteration:
        pass
