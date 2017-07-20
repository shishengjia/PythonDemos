"""
format()方法
但是该方法无法处理缺少某个值的情况
"""

s = '{name} has {n} messages'
print(s.format(name='Tom', n=37)) # Tom has 37 messages
# print(s.format(name='Tom')) # Error


"""
被替换的值能在变量中找到，可以使用forma_mao()和vars()
同样也无法处理缺少某个值的情况
"""
name = 'Tom'
n = 37
print(vars()) # 打印当前调用位置的属性和属性值
print(s.format_map(vars()))

"""
避免出现上面的情况可以单独定义一个带有__missing__()方法的字典
"""


class safasub(dict):
    """
    对于缺少value的key直接返回key的名字
    """
    def __missing__(self, key):
        return '{' + key + '}'

del n # 先确保n不存在
print(s.format_map(safasub(vars()))) # Tom has {n} messages
