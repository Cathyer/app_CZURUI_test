#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2020/1/4 11:09 上午
# software: PyCharm

from appium.webdriver.common.mobileby import MobileBy

class LoginPageLoc:

    # 个人中心我的pdf
    my_pdf_loc = (MobileBy.ID, "com.czur.scanpro:id/user_pdf")

    # 个人中心VIP高级功能
    VIP_function_loc = (MobileBy.ID, "com.czur.scanpro:id/user_vip_and_invite_ll")

    # 自动同步
    auto_sync_loc = (MobileBy.ID, "com.czur.scanpro:id/sync_switch_btn")

    # 现在同步
    synchronize_now_loc = (MobileBy.ID, "com.czur.scanpro: id / user_sync_now_rl")


