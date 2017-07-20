# 当列表的嵌套层数很多时，可以用递归来进行打印输出
# Python3 默认递归层数不能超过100层
import sys
movies = ["Brizalld", 1918, ["Games", ["OverWatch", "HearthStone"]]]

"""
indent： 是否先输出制表符
level: 制表符个数
"""
def print_list(list_, indent=False, level=0, fn=sys.stdout):
    for item in list_:
        if isinstance(item, list):
            print_list(item, indent, level+1, fn)
        else:
            if indent:
                # 输出item前先输出level个制表符
                print("%s" % ("\t" * level), end="", file=fn)
            print(item, file=fn)

print_list(movies,True,1)
