#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/12/13 1:47 下午
# software: PyCharm

import pytest

pytest.main(["-s", "-v", "--html=OutPuts/Reports/one999.html",
             "--reruns", "2", "--reruns-delay", "5",
             "--alluredir=OutPuts/Reports/allure"])


"""
要在测试完成后查看实际报告，您需要使用Allure命令行实用程序从结果生成报告。
allure serve /OutPuts/Reports/allure
"-m", "smoke", 
"""


