# -*- coding: utf-8 -*-
import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: ', ctime())

"""
创建Thread的实例，传给它一个函数
"""


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 实例化Thread对象
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        # 执行线程
        threads[i].start()

    for i in nloops:
        # 调用join方法，等待线程结束
        # 另外join方法在这里不需要调用，join方法只有在需要等待线程完成的时候才是有用的
        threads[i].join()

    print('all done at: ', ctime())

# main()


"""
创建Thread的实例，传给它一个可调用的类实例
比起传递一个函数，有更好的灵活性
"""


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ', ctime())

# main()


"""
派生Thread的子类，并创建子类的实例
"""


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ', ctime())

main()


