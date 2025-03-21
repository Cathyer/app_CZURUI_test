#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Cathy
# datetime:2019/12/7 10:26 上午
# software: PyCharm
from datetime import datetime

from app_CZURsaomiao_test.Common.logger_handler import logger
from app_CZURsaomiao_test.Settings.constant import p_path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver



import time
import datetime


class BasePage:
    """
    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self,locator,img_doc,timeout=30,poll_fre=0.5):
        """
        :param locator: 元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分。${页面名称_行为名称}_当前的时间.png
        :param timeout:
        :param poll_fre:
        :return: None
        """
        logger.info("{} : 等待 {} 元素可见".format(img_doc,locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))

        except:
            # 异常信息写入日志
            logger.exception("等待元素可见失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logger.info("等待结束.开始时间为{},结束时间为:{},一共等待耗时为:{}".format(start,end,end-start))

    # 等待元素存在
    def wait_page_contains_element(self,locator,img_doc,timeout=30,poll_fre=0.5):
        logger.info("{} : 等待 {} 元素存在".format(img_doc,locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except:
            # 异常信息写入日志
            logger.exception("等待元素存在失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logger.info("等待结束.开始时间为{},结束时间为:{},一共等待耗时为:{}".format(start,end,end-start))

    # 查找单个元素
    def get_element(self,locator,img_doc):
        logger.info("{} : 查找 {} 元素.".format(img_doc,locator))
        try:
            ele = self.driver.find_element(*locator)
        except:
            # 异常信息写入日志
            logger.exception("查找元素失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    def input_text(self,locator,value,img_doc,timeout=30,poll_fre=0.5):
        # 1）等待元素可见；2）查找元素；3）输入动作
        self.wait_ele_visible(locator,img_doc,timeout,poll_fre)
        ele = self.get_element(locator,img_doc)
        logger.info("{}: 对 {} 元素输入文本 {}".format(img_doc,locator,value))
        try:
            ele.send_keys(value)
        except:
            # 异常信息写入日志
            logger.exception("输入文本失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def click_element(self,locator,img_doc,timeout=30,poll_fre=0.5):
        # 1）等待元素可见；2）查找元素；3）点击
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logger.info("{}: 点击 {} 元素 ".format(img_doc,locator))
        try:
            ele.click()
        except:
            # 异常信息写入日志
            logger.exception("点击操作失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def get_element_text(self,locator,img_doc,timeout=30,poll_fre=0.5):
        # 1）等待元素存在；2）查找元素；3）获取动作
        self.wait_ele_visible(locator,img_doc,timeout,poll_fre)
        ele = self.get_element(locator,img_doc)
        logger.info("{}: 获取 {}  元素的文本内容.".format(img_doc,locator))
        try:
            text = ele.text
        except:
            # 异常信息写入日志
            logger.exception("获取元素文本值失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logger.info("获取的文本值为: {}".format(text))
            return text

    def get_element_attribute(self,locator,attr,img_doc,timeout=30,poll_fre=0.5):
        # 1）等待元素存在；2）查找元素；3）获取动作
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logger.info("{}: 获取 {}  元素的属性 {}.".format(img_doc,locator,attr))
        try:
            value = ele.get_attribute(attr)
        except:
            # 异常信息写入日志
            logger.exception("获取元素属性失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logger.info("获取的属性值为: {}".format(value))
            return value

    def check_element_visible(self,locator,img_doc,timeout=10,poll_fre=0.5):
        """
         # 检测元素是否在页面存在且可见。
         如果退出元素存在，则返回True。否则返回False
        :return: 布尔值
        """
        logger.info("{}: 检测元素 {} 存在且可见于页面。".format(img_doc,locator))
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            logger.exception(" {}秒内元素在当前页面不可见。".format(timeout))
            self.save_page_screenshot(img_doc)
            return False
        else:
            logger.info(" {}秒内元素可见。".format(timeout))
            return True

    def get_element_toast_text(self, locator, img_doc, timeout=10, poll_fre=0.01):
        """

        :param locator:
        :param img_doc:
        :param timeout:
        :param poll_fre:
        :return:
        """
        logger.info("{}: 检测元素 {} 存在于页面。".format(img_doc,locator))
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.presence_of_element_located(locator))
            ele = self.get_element(locator, img_doc)
            text = ele.text
        except:
            logger.exception(" {}秒内元素在当前页面不存在。".format(timeout))
            self.save_page_screenshot(img_doc)
            return False
        else:
            logger.info(" {}秒内元素存在。".format(timeout))
            return text

    # 切换到新的窗口？ 动作：导致新的窗口出现。
    def switch_to_new_window(self):
        # 等待新窗口出现
        time.sleep(2)
        # 获取窗口的句柄，切换进新的窗口
        wins = self.driver.window_handles
        logger.info("xxxxx")
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            pass

    # 动作：触发alert出现 。
    def handle_alert(self,action="accept"):
        # 等待alert出现
        # 切换到alert
        # 关闭alert? accept，dismiss??
        pass


    def get_window_handles(self):
        pass

    def get_current_url(self):
        pass

    def save_page_screenshot(self,img_doc):
        """
        :param img_doc:
        :return:
        """
        # 路径配置文件中引入图片保存路径  + 年月日-时分秒
        #  # 截图 - 命名。 页面名称_行为名称_当前的时间.png
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = p_path.SCREENSHOT_PATH + "/{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logger.exception("当前网页截图失败")
        else:
            logger.info("截取当前网页成功并存储在: {}".format(screenshot_path))