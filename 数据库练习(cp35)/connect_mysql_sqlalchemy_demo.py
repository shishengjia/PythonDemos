# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine("mysql://root:ssjusher123@127.0.0.1/news?charset=utf8")
# 基类
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Post(Base):
    """
    新闻类型 
    """
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), default='')
    author = Column(String(20))
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime)
    is_valid = Column(Boolean, default=True)

# 创建表
# Base.metadata.create_all(engine)


class Test:
    def __init__(self):
        self.session = Session()

    def add_one(self):
        """
        添加数据
        """
        new_obj = Post(
            title='你好',
            content='1234567',
            types='music',
            author='SSJ',
            created_at=datetime.now(),
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_by_id(self, id):
        return self.session.query(Post).get(id)

    def get_by_types(self, type):
        return self.session.query(Post).filter_by(types=type)

    def update_title(self, ID, title):
        obj = self.session.query(Post).get(ID)
        if obj:
            obj.title = title
            self.session.add(obj)
            self.session.commit()
            return True
        return False



obj = Test()
# rest = obj.get_by_id(1)
# print(rest.title)
# rest = obj.get_by_types('music')
# if rest:
#     for item in rest:
#         print(item.title)
obj.update_title(1, '守望先锋系列音乐')