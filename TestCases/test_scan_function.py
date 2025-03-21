#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
from PageObjects.main_window import MainWindow
from Settings.config import Config

class TestScanFunction:
    """扫描功能测试类"""
    
    @pytest.fixture(scope="function")
    def main_window(self):
        """初始化主窗口"""
        window = MainWindow()
        assert window.launch_app(), "启动应用失败"
        yield window
        window.close_app()
    
    def test_basic_scan(self, main_window):
        """测试基本扫描功能"""
        # 点击扫描按钮
        assert main_window.click_scan_button(), "点击扫描按钮失败"
        
        # 等待扫描完成
        assert main_window.wait_for_scan_complete(), "扫描未完成"
        
        # 保存文档
        file_name = "test_scan_" + Config.get_test_config("timestamp") + ".pdf"
        assert main_window.save_scanned_document(file_name), "保存文档失败"
    
    @pytest.mark.parametrize("mode", ["color", "grayscale", "black_white"])
    def test_scan_modes(self, main_window, mode):
        """测试不同扫描模式"""
        # 选择扫描模式
        assert main_window.select_scan_mode(mode), f"选择{mode}模式失败"
        
        # 点击扫描按钮
        assert main_window.click_scan_button(), "点击扫描按钮失败"
        
        # 等待扫描完成
        assert main_window.wait_for_scan_complete(), "扫描未完成"
        
        # 保存文档
        file_name = f"test_scan_{mode}_" + Config.get_test_config("timestamp") + ".pdf"
        assert main_window.save_scanned_document(file_name), "保存文档失败"
    
    @pytest.mark.parametrize("dpi", [200, 300, 600])
    def test_scan_resolutions(self, main_window, dpi):
        """测试不同扫描分辨率"""
        # 设置分辨率
        assert main_window.set_resolution(dpi), f"设置{dpi}DPI分辨率失败"
        
        # 点击扫描按钮
        assert main_window.click_scan_button(), "点击扫描按钮失败"
        
        # 等待扫描完成
        assert main_window.wait_for_scan_complete(), "扫描未完成"
        
        # 保存文档
        file_name = f"test_scan_{dpi}dpi_" + Config.get_test_config("timestamp") + ".pdf"
        assert main_window.save_scanned_document(file_name), "保存文档失败"
    
    def test_settings_dialog(self, main_window):
        """测试设置对话框"""
        # 点击设置按钮
        assert main_window.click_settings_button(), "点击设置按钮失败"
        
        # TODO: 添加设置对话框的具体测试步骤
        
        # 关闭设置对话框
        main_window.press_key('escape') 