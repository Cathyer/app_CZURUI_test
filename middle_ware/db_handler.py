#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/10/22 3:55 下午
# software: PyCharm
from pymysql.cursors import DictCursor

from app_CZURsaomiao_test.Common.config_handler import config
from app_CZURsaomiao_test.Common.db_handler import DBHandler


class MyDBHandler(DBHandler):
    def __init__(self, **kw):
        super().__init__(
            host=config.read('db', 'host'),
            port=eval(config.read('db', 'port')),
            user=config.read('db', 'user'),
            password=config.read('db', 'password'),
            charset=config.read('db', 'charset'),
            database=config.read('db', 'database'),
            cursorclass=DictCursor,
            **kw
        )
