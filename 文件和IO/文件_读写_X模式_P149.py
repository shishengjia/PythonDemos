"""
x模式
只对不存在的文件进行写入操作，如果文件已存在，则抛出异常
下面的例子中，第一次执行将会创建somefile.text文件并写入内容，但后面的运行都会抛出异常
"""

try:
    with open('../somefile.text', 'xt') as f:
        f.write("Hello World\n")
except FileExistsError as e:
    print("File already exists")
