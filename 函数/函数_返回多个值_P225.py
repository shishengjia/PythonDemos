
def myfun():
    return 1, 2, 3

# myfun实际上返回的是一个元组

# 元组解包，依次赋值给a，b，c三个元素
a, b, c = myfun()
# 直接赋值给d
d = myfun()