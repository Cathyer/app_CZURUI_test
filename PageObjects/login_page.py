#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2020/1/3 9:31 上午
# software: PyCharm
from app_CZURsaomiao_test.Common.basepage import BasePage
from app_CZURsaomiao_test.PageLocators.login_page_loc import LoginPageLoc


class LoginPage(BasePage):

    def enters_login(self):
        self.click_element(LoginPageLoc.my_icon_loc, "主页面_点击我的图标")
        self.click_element(LoginPageLoc.login_reg_loc, "我的页面_点击登录/注册按钮")

    def login(self, username, password):
        self.enters_login()
        self.input_text(LoginPageLoc.login_user_name_loc, username, "登录页面_输入用户名")
        self.input_text(LoginPageLoc.login_user_password_loc, password, "登录页面_输入密码")
        self.click_element(LoginPageLoc.login_button_loc, "登录页面_点击登录按钮")

    def check_my_pdf_exist(self):
        return self.check_element_visible(LoginPageLoc.my_pdf_loc, "个人中心_我的PDF存在")

    def get_toast_password_len_error(self):
        return self.get_element_toast_text(LoginPageLoc.error_password_len_toast_loc, "登录页面_获取密码不合法toast信息")

    def get_toast_password_error(self):
        return self.get_element_toast_text(LoginPageLoc.error_password_toast_loc, "登录页面_获取密码错误toast信息")

    def get_toast_username_error(self):
        return self.get_element_toast_text(LoginPageLoc.error_username_toast_loc, "登录页面_获取用户名不合法toast信息")





