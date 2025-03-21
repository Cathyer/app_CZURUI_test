#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/10/7 8:02 下午
# software: PyCharm
import logging
import os
from datetime import datetime

from app_CZURsaomiao_test.Settings.constant import p_path


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(funcName)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                 **kw
                 ):
        """初始化函数。完成 level, format, handler 配置"""
        # 子类的初始化使用了父类的 # Dog, eating
        super().__init__(name, level=level)

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)
        # handler 的级别
        handler.setLevel(handler_level)
        # 添加 handler
        self.addHandler(handler)
        # 设置 format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


# log文件输出到指定目录,按天输出
# date_name = datetime.now().strftime("%Y-%m-%d")
# file_name = os.path.join(p_path.LOGS_PATH, '{}.txt'.format(date_name))
# logger = LoggerHandler('成者云web自动化', 0, file_name)

# logger.info('hhhhh')
logger = LoggerHandler('成者扫喵app android自动化')

