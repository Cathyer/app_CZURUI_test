#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/10/22 3:24 下午
# software: PyCharm

import pymysql


class DBHandler:
    def __init__(self,
                 host=None,
                 port=3306,
                 user='root',
                 password='',
                 charset='utf8',
                 database=None,
                 **kw
                 ):
        """初始化数据库"""
        # conn = pymysql.connect(
        #     host='120.78.128.25',
        #     port=3306,
        #     user='future',
        #     password='123456',
        #     charset='utf8',  # 不能是 utf-8
        #     database='futureloan'
        # )
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,  # 不能是 utf-8
            database=database,
            **kw
        )
        self.cursor = self.conn.cursor()

    def query_one(self, sql, args=None):
        """查询数据库一条记录"""
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.fetchone()

    def query_all(self, sql, args=None):
        """查询数据库一条记录"""
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.fetchall()

    def query(self, sql, args=None, one=True):
        """主体查询函数"""
        if one:
            return self.query_one(sql, args)
        return self.query_all(sql, args)

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    qu = DBHandler(host='60.205.140.103',
             port=3306,
             user='root',
             password='Changer008',
             charset='utf8',  # 不能是 utf-8
             database='changer_passport_db'
                   )
    print(qu.query_one('SELECT * FROM account;'))
    qu.close()
