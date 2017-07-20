# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class Test:
    def __init__(self):
        """
        连接MongoClient
        由3中方法可以选择，看使用情况
        """
        # 简写
        self.client = MongoClient()
        # 指定端口和地址
        # self.client = MongoClient('127.0.0.1', 27017)
        # 使用URI
        # self.client = MongoClient('mongodb://127.0.0.1:27017/')

        # 选择数据库
        self.db = self.client['test']

    def add_one(self, title, number, created_time=datetime.now()):
        """
        添加一条数据
        需要注意的是Mongo中不需要事先建立表，插入数据的同时直接根据所传入字典对象的内容生成表
        """
        # 创建一个字典对象
        post = {
            'title': title,
            'number': number,
            'created_time': created_time
        }
        # 指定将数据添加到blog下的post表
        return self.db.blog.post.insert_one(post)

    def find_by_id(self, post_id):
        """
        通过ID查找数据
        Mongo中自动生成的ID主键是ObjectId(id)的形式，所以在查询的时候要遵循该格式
        从bson.objectid导入ObjectId
        """
        return self.db.blog.post.find_one({'_id': ObjectId(post_id)})

    def update_number(self, post_id, number):
        """
        更新一条数据
        在update_one函数中，通过第一个参数查找更新对象，通过第二个参数对查找到的对象进行更新
        下面语句的含义是对指定ID的数据的number字段加上一个number值,通过 $inc 实现
        """
        return self.db.blog.post.update_one({'_id': ObjectId(post_id)}, {'$inc': {'number': number}})

    def update_all_number(self, number):
        """
        批量更新
        update_many函数参数的作用同update_one
        {} 表示没有查找限制，更新全部的数据
        """
        return self.db.blog.post.update_many({}, {'$inc': {'number': number}})

    def delete_by_id(self, post_id):
        """
        根据ID删除，同样注意id值的格式
        """
        return self.db.blog.post.delete_one({'_id': ObjectId(post_id)})


t = Test()
# [t.add_one('test{}'.format(x), x) for x in range(1, 10)]
t.delete_by_id('5967665756f1fa1cc86296c2')