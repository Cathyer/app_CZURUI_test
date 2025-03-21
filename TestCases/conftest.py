#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/12/13 11:48 上午
# software: PyCharm
from appium import webdriver
import pytest

from CZUR_Clound_web_test.PageObjects.login_page import LoginPage
from CZUR_Clound_web_test.TestDatas import Common_Datas as CD


@pytest.fixture
def init_driver():
    desired_caps = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "oppo R11s",
        "appActivity": "com.czur.scanpro.ui.base.WelcomeActivity",
        "appPackage": "com.czur.scanpro",
        "noReset": True  # 应用不重置
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    yield driver
    driver.quit()























#
#
# # 初始化LoginPage driver
# @pytest.fixture
# def web_login_page_driver(init_driver):
#     lp = LoginPage(init_driver)
#     yield {'driver': init_driver, 'lp' : lp}
#
#
# # 登录前置
# @pytest.fixture
# def web_login(init_driver):
#     LoginPage(init_driver).login(CD.user, CD.password)
#     yield init_driver
#
# # 注册前置
# @pytest.fixture
# def register_pre(init_driver):
#     LoginPage(init_driver).enter_register_page()
#     yield init_driver
#
#
#
# @pytest.fixture(scope="class")
# def demo():
#     print("============测试类级别：用例开始==========")
#     yield
#     print("============测试类级别：用例结束==========")