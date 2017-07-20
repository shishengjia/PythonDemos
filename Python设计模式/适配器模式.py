# -*- coding: utf-8 -*-
"""
适配器模式（Adapter pattern）是一种结构型设计模式，帮助我们实现两个不兼容接口之间
的兼容
通常两个不兼容接口中的一个是他方的或者是老旧的。
如果一个接口是他方的，就意味着我们无法访问其源代码。如果是老旧的，那么对其重构通常是
不切实际的
"""


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'Computer is running'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'I am a humna'


class Adapter:
    def __init__(self, obj, adapted_method):
        self.obj = obj
        self.name = obj.name
        # 将需要包装的方法添加到内部字典中
        self.__dict__.update(adapted_method)
        print(self.__dict__)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    human = Human('Bob')
    # 将human类中的speak方法适配，统一接口
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

    for i in objects:
        print(i.name)

main()