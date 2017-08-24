import redis


class TestString:

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def set(self, key, value):
        """
        set 设置值
        """
        return self.r.set(key, value)

    def get(self, key):
        """
        get 获取值
        """
        return self.r.get(key)

    def mset(self, kvs):
        """
        mset 设置多个键值对，以字典的形式
        """
        return self.r.mset(kvs)

    def mget(self, keys):
        """
        获取多个键值对， 传入键组成的列表
        """
        return self.r.mget(keys)

    def delete(self, key):
        """
        删除指定的键值对
        """
        return self.r.delete(key)

    def append(self, key, value):
        """
        直接在后面追加相应字符
        """
        return self.r.append(key, value)

    def increase(self, key, inc_number=1):
        """
        只有整数或者整数字符串能调用该方法，否则或抛出异常
        """
        try:
            if self.r.get(key):
                self.r.incr(key, inc_number)
        except redis.ResponseError as e:
            print(e)


class TestList:

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)


def main():
    obj = TestString()
    obj.set('test2', 1.1)
    # print(obj.get('x'))
    # obj.mset({'y': 12, 'z': 13})
    # print(obj.mget(['x', 'y', 'z']))
    print(obj.get('test2'))


if __name__ == '__main__':
    main()