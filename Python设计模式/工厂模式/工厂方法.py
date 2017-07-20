# -*- coding: utf-8 -*-
"""
工厂方法（Factory Method），它是一个方法（或以地道的Python
术语来说，是一个函数），对不同的输入参数返回不同的对象
在工厂方法模式中，我们执行单个函数，传入一个参数（提供信息表明我们想要什么），但
并不要求知道任何关于对象如何实现以及对象来自哪里的细节。
"""

import xml.etree.ElementTree as etree
import json


class JSONConnector:
    """
    解析JSON文件，通过parsed_data()方法以一个字典的形式返回数据
    """
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    """
    解析XML文件，通过parsed_data()方法以xml.etree.ElementTree列表的形式返回所有数据
    """
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(file_path):
    """
    工厂方法，基于输入文件路径的扩展名返回对应connector实例
    """
    if file_path.endswith('json'):
        connector = JSONConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector(file_path)


def connect_to(file_path):
    """
    对connection_factory进行包装，添加异常处理
    """
    factory = None
    try:
        factory = connection_factory(file_path)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('person.sq3')
    print()

    xml_factory = connect_to('./person.xml')
    xml_data = xml_factory.parsed_data

    # 查找所有lastName为Liar的person元素
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))

    # 打印其姓名,电话号码信息和地址信息
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
        [print('{} : {}'.format(a.tag, a.text)) for a in liar.find('address')]
    print()

    # 展示所有甜甜圈的named，price，topping
    json_factory = connect_to('./donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: {}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()
