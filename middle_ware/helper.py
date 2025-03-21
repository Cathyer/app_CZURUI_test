#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/10/24 9:31 上午
# software: PyCharm
import random
from app_CZURsaomiao_test.middle_ware.db_handler import MyDBHandler

# 生成随机手机号


def mk_phone():
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for n in range(9):
        number = str(random.randint(0, 9))
        phone += number
    db = MyDBHandler()
    while True:
        user = db.query('SELECT * FROM account WHERE mobile=%s;',
                        args=[phone, ])
        if not user:
            break
    return phone

a = mk_phone()
print(a)






