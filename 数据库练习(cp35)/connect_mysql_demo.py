# -*- coding: utf-8 -*-
import MySQLdb


class MySQLTool:
    def __init__(self):
        self.conn = self.get_connection()
        self.cursor = self.conn.cursor()

    def get_connection(self):
        """
        链接数据库
        """
        try:
            conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='ssjusher123',
                db='news',
                port=3306,
                charset='UTF8'
            )
            print('成功链接数据库')
            return conn
        except MySQLdb.Error as e:
            print('Error : {}'.format(e))

    def close_connection(self):
        """
        关闭数据库
        """
        try:
            if self.conn:
                self.conn.close()
                self.cursor.close()
                print('成功关闭数据库')
        except MySQLdb.Error as e:
            print('Error : {}'.format(e))

    def get_by_type(self, type):
        sql = 'select * from news where `type` = %s'
        self.cursor.execute(sql, (type,))
        return [dict(zip([k[0] for k in self.cursor.description], row)) for row in self.cursor.fetchall()]

    def get_by_title(self, search):
        sql = 'select * from news where `title` LIKE "%' + search + '%"'
        self.cursor.execute(sql)
        return [dict(zip([k[0] for k in self.cursor.description], row)) for row in self.cursor.fetchall()]

    def delete(self, news_id):
        sql = 'update news set `is_valid`=0 where `id` = %s'
        self.cursor.execute(sql, (news_id,))
        self.conn.commit()
        return True

    def restore(self, news_id):
        sql = 'update news set `is_valid`=1 where `id` = %s'
        self.cursor.execute(sql, (news_id,))
        self.conn.commit()
        return True

    def inster(self, title, content, author, image, type):
        try:
            sql = 'insert into news (`title`, `content`, `author`, `image`, `type`) ' \
                  'value(%s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (title, content, author, image, type))
            self.conn.commit()
        except MySQLdb.Error as e:
            print('Error : {}'.format(e))
            self.conn.rollback()



mst = MySQLTool()
# data = mst.get_by_type(3)
# data2 = mst.get_by_title('比伯')
# for item in data2:
#     print(item['title'])
mst.inster('test', '2131323', 'kkk', '', 1)
mst.close_connection()