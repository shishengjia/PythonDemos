"""
使用translate()函数
"""

# 先构建一个转换表,\t,\f替换为空格，\r完全删除
rmap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}

s = 'pyth̃on\fis\tawsome\r\n'
a = s.translate(rmap)
print(a) # pyth̃on is awsome

# 再进一步把Unicode组合字符去掉
import unicodedata
import sys

# 通过dict的formkeys()函数构建了一个将每个Unicode组合字符都映射为None的字典
# unicodedata.combining()函数判断是否为组合字符
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# 对文本的形式进行规范，使其为NFD组合字符形式
b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs)) # python is awsome


"""
另一种清理文本的技术，当最终目标是ASCII形式的文本时才有效
"""
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii')) # python is awsome


"""
对于简单的替换操作，即使必须多次调用，str.replace()通常是最快的
如果需要做任何高级的操作，如字符到字符的重映射或删除，那么translate()函数是非常快的
"""
