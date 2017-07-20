# 一次IO读入的数据量
CHUNKSIZE = 40

with open('../test.txt', 'rt') as reader:
    # iter第二个参数指定哨兵(结束)值
    for data in iter(lambda: reader.read(CHUNKSIZE), ''):
        print(data)
