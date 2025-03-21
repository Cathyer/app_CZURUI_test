#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/10/7 8:02 下午
# software: PyCharm

import os
from datetime import datetime


class ProjectPath:

    # 项目路径
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 输出路径
    OUT_PUTS_PAT = os.path.join(ROOT_PATH, 'OutPuts')
    # 测试报告路径
    REPORT_PATH = os.path.join(OUT_PUTS_PAT, 'Reports')
    # Logs路径
    LOGS_PATH = os.path.join(OUT_PUTS_PAT, 'Logs')
    # 截图路径
    SCREENSHOT_PATH = os.path.join(OUT_PUTS_PAT, 'Screenshots')
    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, 'Settings')
    # 如果没有改文件夹，自动创建
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

    # 没有log目录就创建
    if not os.path.exists(LOGS_PATH):
        os.mkdir(LOGS_PATH)
    # 没有截图目录就创建
    if not os.path.exists(SCREENSHOT_PATH):
        os.mkdir(SCREENSHOT_PATH)


p_path = ProjectPath()
# print(p_path.SCREENSHOT_PATH)
# screenshot_path = os.path.join(p_path.SCREENSHOT_PATH, '{}_{}.png'.format('img_doc', datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))
# print(screenshot_path)