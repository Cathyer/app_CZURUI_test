#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2020/1/3 9:30 上午
# software: PyCharm
import pytest

from app_CZURsaomiao_test.PageObjects.login_page import LoginPage
from app_CZURsaomiao_test.TestDatas import Common_Datas as CD
from app_CZURsaomiao_test.TestDatas import login_datas as LD


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.parametrize("fail_user_datas", LD.fail_user_datas)
    def test_login_user_fail(self, fail_user_datas, init_driver):
        LoginPage(init_driver).login(fail_user_datas["user"], fail_user_datas["passwd"])
        assert LoginPage(init_driver).get_toast_username_error() == fail_user_datas["expect"]

    @pytest.mark.parametrize("fail_passwd_lenth_datas", LD.fail_passwd_lenth_datas)
    def test_login_password_lenth_fail(self, fail_passwd_lenth_datas, init_driver):
        LoginPage(init_driver).login(fail_passwd_lenth_datas["user"], fail_passwd_lenth_datas["passwd"])
        assert LoginPage(init_driver).get_toast_password_len_error() == fail_passwd_lenth_datas["expect"]

    @pytest.mark.parametrize("fail_passwd_datas", LD.fail_passwd_datas)
    def test_login_password_fail(self, fail_passwd_datas, init_driver):
        LoginPage(init_driver).login(fail_passwd_datas["user"], fail_passwd_datas["passwd"])
        assert LoginPage(init_driver).get_toast_password_error() == fail_passwd_datas["expect"]

    @pytest.mark.smoke
    def test_login_success(self, init_driver):
        LoginPage(init_driver).login(CD.user, CD.password)
        assert LoginPage(init_driver).check_my_pdf_exist()





