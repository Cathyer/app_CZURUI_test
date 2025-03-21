#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime

class Config:
    """配置类"""
    
    # 基础目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 输出目录
    OUTPUT_DIR = os.path.join(BASE_DIR, "Outputs")
    REPORT_DIR = os.path.join(OUTPUT_DIR, "Reports")
    LOG_DIR = os.path.join(OUTPUT_DIR, "Logs")
    SCREENSHOT_DIR = os.path.join(OUTPUT_DIR, "Screenshots")
    
    # 测试数据目录
    TEST_DATA_DIR = os.path.join(BASE_DIR, "TestDatas")
    TEST_CASE_DIR = os.path.join(BASE_DIR, "TestCases")
    PAGE_OBJECT_DIR = os.path.join(BASE_DIR, "PageObjects")
    PAGE_LOCATOR_DIR = os.path.join(BASE_DIR, "PageLocators")
    COMMON_DIR = os.path.join(BASE_DIR, "Common")
    MIDDLEWARE_DIR = os.path.join(BASE_DIR, "middle_ware")
    
    # 测试配置
    TEST_CONFIG = {
        "timeout": 30,  # 默认超时时间（秒）
        "interval": 0.5,  # 重试间隔（秒）
        "similarity_threshold": 0.9,  # 图像匹配相似度阈值
        "retry_times": 3,  # 失败重试次数
        "retry_delay": 1,  # 重试延迟（秒）
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S")  # 时间戳
    }
    
    # 应用配置
    APP_CONFIG = {
        "name": "CZUR Scanner",  # 应用名称
        "version": "1.0.0",  # 应用版本
        "window_title": "CZUR Scanner",  # 窗口标题
        "app_path": "/usr/bin/czur-scanner",  # 应用路径
        "log_level": "INFO"  # 日志级别
    }
    
    @classmethod
    def get_test_config(cls, key):
        """获取测试配置"""
        return cls.TEST_CONFIG.get(key)
    
    @classmethod
    def get_app_config(cls, key):
        """获取应用配置"""
        return cls.APP_CONFIG.get(key)
    
    @classmethod
    def create_dirs(cls):
        """创建必要的目录"""
        dirs = [
            cls.OUTPUT_DIR,
            cls.REPORT_DIR,
            cls.LOG_DIR,
            cls.SCREENSHOT_DIR,
            cls.TEST_DATA_DIR
        ]
        for dir_path in dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
    
    @classmethod
    def get_log_file(cls):
        """获取日志文件路径"""
        timestamp = cls.get_test_config("timestamp")
        return os.path.join(cls.LOG_DIR, f"test_{timestamp}.log")
    
    @classmethod
    def get_report_file(cls):
        """获取报告文件路径"""
        timestamp = cls.get_test_config("timestamp")
        return os.path.join(cls.REPORT_DIR, f"report_{timestamp}.html")
    
    @classmethod
    def get_screenshot_file(cls, name):
        """获取截图文件路径"""
        timestamp = cls.get_test_config("timestamp")
        return os.path.join(cls.SCREENSHOT_DIR, f"{name}_{timestamp}.png") 