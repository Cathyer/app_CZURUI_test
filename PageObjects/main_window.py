#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Common.ui_operator import UIOperator
from Settings.config import Config

class MainWindow(UIOperator):
    """主窗口页面对象"""
    
    def __init__(self):
        super().__init__()
        self.window_title = Config.get_app_config("window_title")
        self.test_data_dir = Config.TEST_DATA_DIR
    
    def launch_app(self):
        """启动应用"""
        app_path = Config.get_app_config("app_path")
        self.process = self.start_application(app_path)
        return self.wait_for_window()
    
    def close_app(self):
        """关闭应用"""
        if hasattr(self, 'process'):
            self.close_application(self.process)
    
    def wait_for_window(self):
        """等待主窗口出现"""
        window = self.get_window_by_title(self.window_title)
        return window is not None
    
    def click_scan_button(self):
        """点击扫描按钮"""
        image_path = os.path.join(self.test_data_dir, "buttons/scan_button.png")
        location = self.find_element_by_image(image_path)
        if location:
            return self.click_element(location)
        return False
    
    def click_settings_button(self):
        """点击设置按钮"""
        image_path = os.path.join(self.test_data_dir, "buttons/settings_button.png")
        location = self.find_element_by_image(image_path)
        if location:
            return self.click_element(location)
        return False
    
    def select_scan_mode(self, mode):
        """选择扫描模式"""
        mode_button_path = os.path.join(self.test_data_dir, f"buttons/{mode}_mode_button.png")
        location = self.find_element_by_image(mode_button_path)
        if location:
            return self.click_element(location)
        return False
    
    def set_resolution(self, dpi):
        """设置扫描分辨率"""
        # 点击分辨率下拉框
        dpi_dropdown_path = os.path.join(self.test_data_dir, "buttons/dpi_dropdown.png")
        location = self.find_element_by_image(dpi_dropdown_path)
        if not location or not self.click_element(location):
            return False
            
        # 选择指定的DPI选项
        dpi_option_path = os.path.join(self.test_data_dir, f"options/{dpi}dpi_option.png")
        location = self.find_element_by_image(dpi_option_path)
        if location:
            return self.click_element(location)
        return False
    
    def wait_for_scan_complete(self):
        """等待扫描完成"""
        complete_image_path = os.path.join(self.test_data_dir, "status/scan_complete.png")
        location = self.find_element_by_image(complete_image_path, timeout=60)
        return location is not None
    
    def save_scanned_document(self, file_name):
        """保存扫描文档"""
        # 点击保存按钮
        save_button_path = os.path.join(self.test_data_dir, "buttons/save_button.png")
        location = self.find_element_by_image(save_button_path)
        if not location or not self.click_element(location):
            return False
            
        # 输入文件名
        self.input_text(file_name)
        self.press_key('enter')
        
        # 等待保存完成
        save_complete_path = os.path.join(self.test_data_dir, "status/save_complete.png")
        location = self.find_element_by_image(save_complete_path, timeout=30)
        return location is not None 