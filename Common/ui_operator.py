#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyautogui
import psutil
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QPoint
from Common.logger import Logger
from Settings.config import Config

class UIOperator:
    """UI 操作基类"""
    
    def __init__(self):
        self.logger = Logger()
        self.timeout = Config.get_test_config("timeout")
        self.interval = Config.get_test_config("interval")
        # 设置 PyAutoGUI 的安全设置
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        # 初始化 Qt 应用
        self.app = QApplication.instance() or QApplication([])
    
    def start_application(self, app_path):
        """启动应用程序"""
        try:
            process = psutil.Popen(app_path)
            self.logger.info(f"启动应用程序: {app_path}")
            time.sleep(2)  # 等待应用启动
            return process
        except Exception as e:
            self.logger.error(f"启动应用程序失败: {str(e)}")
            raise
    
    def close_application(self, process):
        """关闭应用程序"""
        try:
            process.terminate()
            process.wait(timeout=5)
            self.logger.info("关闭应用程序成功")
        except Exception as e:
            self.logger.error(f"关闭应用程序失败: {str(e)}")
            raise
    
    def find_element_by_image(self, image_path, confidence=0.9, timeout=None):
        """通过图像识别查找元素"""
        if timeout is None:
            timeout = self.timeout
            
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    self.logger.info(f"找到元素: {image_path}")
                    return location
                time.sleep(self.interval)
            except Exception as e:
                self.logger.error(f"查找元素失败: {str(e)}")
                time.sleep(self.interval)
        
        self.logger.error(f"未找到元素: {image_path}")
        return None
    
    def click_element(self, location):
        """点击元素"""
        try:
            center = pyautogui.center(location)
            pyautogui.click(center)
            self.logger.info(f"点击元素: {center}")
            return True
        except Exception as e:
            self.logger.error(f"点击元素失败: {str(e)}")
            return False
    
    def double_click_element(self, location):
        """双击元素"""
        try:
            center = pyautogui.center(location)
            pyautogui.doubleClick(center)
            self.logger.info(f"双击元素: {center}")
            return True
        except Exception as e:
            self.logger.error(f"双击元素失败: {str(e)}")
            return False
    
    def input_text(self, text):
        """输入文本"""
        try:
            pyautogui.write(text)
            self.logger.info(f"输入文本: {text}")
            return True
        except Exception as e:
            self.logger.error(f"输入文本失败: {str(e)}")
            return False
    
    def press_key(self, key):
        """按下键盘按键"""
        try:
            pyautogui.press(key)
            self.logger.info(f"按下按键: {key}")
            return True
        except Exception as e:
            self.logger.error(f"按下按键失败: {str(e)}")
            return False
    
    def get_window_by_title(self, title):
        """通过标题获取窗口"""
        try:
            for window in self.app.topLevelWidgets():
                if window.windowTitle() == title:
                    self.logger.info(f"找到窗口: {title}")
                    return window
            self.logger.error(f"未找到窗口: {title}")
            return None
        except Exception as e:
            self.logger.error(f"获取窗口失败: {str(e)}")
            return None
    
    def get_element_by_class(self, window, class_name):
        """通过类名获取元素"""
        try:
            elements = window.findChildren(eval(class_name))
            if elements:
                self.logger.info(f"找到元素: {class_name}")
                return elements[0]
            self.logger.error(f"未找到元素: {class_name}")
            return None
        except Exception as e:
            self.logger.error(f"获取元素失败: {str(e)}")
            return None
    
    def click_position(self, x, y):
        """点击指定位置"""
        try:
            pyautogui.click(x, y)
            self.logger.info(f"点击位置: ({x}, {y})")
            return True
        except Exception as e:
            self.logger.error(f"点击位置失败: {str(e)}")
            return False
    
    def move_to_position(self, x, y):
        """移动鼠标到指定位置"""
        try:
            pyautogui.moveTo(x, y)
            self.logger.info(f"移动鼠标到: ({x}, {y})")
            return True
        except Exception as e:
            self.logger.error(f"移动鼠标失败: {str(e)}")
            return False
    
    def drag_to_position(self, x, y):
        """拖动鼠标到指定位置"""
        try:
            pyautogui.dragTo(x, y)
            self.logger.info(f"拖动鼠标到: ({x}, {y})")
            return True
        except Exception as e:
            self.logger.error(f"拖动鼠标失败: {str(e)}")
            return False
    
    def take_screenshot(self, save_path):
        """截取屏幕截图"""
        try:
            pyautogui.screenshot(save_path)
            self.logger.info(f"截图保存到: {save_path}")
            return True
        except Exception as e:
            self.logger.error(f"截图失败: {str(e)}")
            return False 