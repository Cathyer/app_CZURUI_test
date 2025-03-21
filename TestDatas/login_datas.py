#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2020/1/3 2:38 下午
# software: PyCharm

# 用户格式手机号格式/邮箱格式
fail_user_datas = [{"user":"yiyyiyiy", "passwd":"123456789", "expect": "手机或邮箱格式错误"},
              {"user":"11111111111", "passwd":"123456789", "expect": "手机或邮箱格式错误"},
              ]

# 密码长度不够6位
fail_passwd_lenth_datas = [{"user":"18909855297", "passwd":"1234", "expect": "密码为6-20位字母或数字"},
              {"user":"jiying@czur.com", "passwd":"uuuu", "expect": "密码为6-20位字母或数字"},
              ]

# 密码错误
fail_passwd_datas = [{"user":"18909855297", "passwd":"12347777777", "expect": "用户名或密码错误"},
              {"user":"jiying@czur.com", "passwd":"123999999", "expect": "用户名或密码错误"},
              ]