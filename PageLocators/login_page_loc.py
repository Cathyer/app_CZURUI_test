#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2020/1/3 9:32 上午
# software: PyCharm

from appium.webdriver.common.mobileby import MobileBy

class LoginPageLoc:


    # 主页面我的头像
    my_icon_loc = (MobileBy.ID, "com.czur.scanpro:id/index_user_head_img")

    # 登录注册按钮
    login_reg_loc = (MobileBy.ID, "com.czur.scanpro:id/login_name")

    # 输入账号
    login_user_name_loc = (MobileBy.ID, "com.czur.scanpro:id/login_user_name_edt")

    # 输入密码
    login_user_password_loc = (MobileBy.ID, "com.czur.scanpro:id/login_user_password_edt")

    # 登录
    login_button_loc = (MobileBy.ID, "com.czur.scanpro:id/login_btn")

    # 密码错误长度的toast信息
    error_password_len_toast_loc = (MobileBy.XPATH, '//*[contains(@text,"密码为6-20位字母或数字")]')

    # 用户名不合法toast信息
    error_username_toast_loc = (MobileBy.XPATH, '//*[contains(@text,"手机或邮箱格式错误")]')

    # 密码错误
    error_password_toast_loc = (MobileBy.XPATH, '//*[contains(@text,"用户名或密码错误")]')

    # 个人中心我的pdf
    my_pdf_loc = (MobileBy.ID, "com.czur.scanpro:id/user_pdf")

    # 个人中心VIP高级功能




