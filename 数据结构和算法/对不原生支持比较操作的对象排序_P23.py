"""
首先lambda表达式可以解决问题
这里使用attrgetter，速度更快，而且可以同时提取多个值进行比较，和字典的itemgetter使用类似
"""
from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(5), User(16)]
print(sorted(users, key=attrgetter('user_id')))
