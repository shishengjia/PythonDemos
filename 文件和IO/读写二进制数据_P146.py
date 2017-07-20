"""
二进制数据的读写，rb和wb模式
读取二进制数据，所有的数据将以二进制形式返回
同样，写入二进制数据时，数据必须以对象形式来提供，该对象可以将数据以字节形式暴露出来
"""
with open('example.bin', 'rb') as f:
    data = f.read()

with open('example.bin', 'wb') as f:
    f.write(b'Hello World')

"""
在做索引操作时，字节串会返回代表该字节的整数值而不是字符串
"""
b = b'Hello World'
for x in b:
    print(x, end=" ") # 72 101 108 108 111 32 87 111 114 108 100


"""
在二进制文件中读取或写入文本内容，要进行编码和解码操作
"""
with open('example.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('example.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
