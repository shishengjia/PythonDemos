# -*- coding: utf-8 -*-
from mongoengine import connect, Document, EmbeddedDocument, StringField\
    , IntField, FloatField, ListField, EmbeddedDocumentField

# 链接数据库

# 简写，默认链接本地数据库
connect('test')

# 指定端口和地址
connect('test', host='127.0.0.1', port=27017)

# 使用URI
connect('test', host='mongodb://localhost/post')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


class Grade(EmbeddedDocument):
    """
    学生成绩
    """
    name = StringField(max_length=100, required=True)
    score = FloatField(required=True)


class Student(Document):
    """
    学生模型
    """
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students'
    }

    def get_one(self):
        """
        查询满足条件的第一条数据
        """
        return Student.objects.first()

    def get_all(self):
        """
        查询所有数据
        """
        return Student.objects.all()

    def get_by_oid(self, oid):
        """
        根据ID查询数据
        """
        return Student.objects.filter(pk=oid).first()

    def update(self):
        """
        修改数据
        """
        # 修改一条数据
        # rest = Student.objects.filter(sex='male').update_one(inc__age=1)
        # return rest

        # 修改多条数据
        rest = Student.objects.filter(sex='male').update(inc__age=1)
        return rest

    def delete(self):
        """
        删除数据
        """
        # 删除一条数据
        rest = Student.objects.filter(sex='male').first.delete()

        # 删除多条数据
        rest = Student.objects.filter(sex='male').delete()

    def add_one(self):
        """
        新增一条数据
        """
        chinese = Grade(
            name='语文',
            score=123,
        )
        english = Grade(
            name='英语',
            score=99,
        )

        stu_obj = Student(
            name='ssj',
            age=22,
            sex='male',
            grades=[chinese, english],
        )

        stu_obj.save()
        return stu_obj

t = Student()
t.add_one()