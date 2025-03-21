# CZUR 扫描仪应用自动化测试项目

## 项目简介
本项目是 CZUR 扫描仪应用的自动化测试框架，基于 Python + Pytest 开发，采用 Page Object Model (POM) 设计模式，实现了测试用例的自动化执行、报告生成等功能。

## 项目架构
```
app_CZURsaomiao_test/
├── Common/           # 公共组件层
├── PageLocators/    # 页面定位器层
├── PageObjects/     # 页面对象层
├── TestCases/       # 测试用例层
├── TestDatas/       # 测试数据层
├── Settings/        # 配置层
├── Outputs/         # 输出层（测试报告、日志）
├── middle_ware/     # 中间件层
└── main_pytest.py   # 测试执行入口
```

## 技术栈
- Python 3.x
- Pytest
- Page Object Model
- Allure 报告
- HTML 报告

## 环境要求
- Python 3.x
- pip 包管理器
- 虚拟环境（推荐）

## 安装步骤

1. 克隆项目
```bash
git clone [项目地址]
cd app_CZURsaomiao_test
```

2. 创建并激活虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法

### 运行测试
```bash
python main_pytest.py
```

### 查看测试报告
1. HTML 报告
   - 报告位置：`Outputs/Reports/one999.html`
   - 直接在浏览器中打开查看

2. Allure 报告
```bash
allure serve Outputs/Reports/allure
```

## 项目特点
- 采用 Page Object Model 设计模式
- 支持测试用例失败重试
- 自动生成测试报告
- 模块化的项目结构
- 清晰的代码组织

## 目录说明

### PageObjects/
- 包含所有页面对象类
- 封装页面元素和操作
- 实现页面业务逻辑

### PageLocators/
- 存放页面元素定位信息
- 将元素定位与页面操作分离

### TestCases/
- 包含所有测试用例
- 实现测试场景
- 包含测试夹具（fixtures）

### TestDatas/
- 存放测试数据
- 支持数据驱动测试

### Common/
- 公共工具类
- 通用方法
- 辅助函数

### Settings/
- 项目配置文件
- 环境配置
- 常量定义

### Outputs/
- 测试报告
- 日志文件
- 测试结果

## 测试用例编写规范

1. 命名规范
   - 测试文件：`test_*.py`
   - 测试类：`Test*`
   - 测试方法：`test_*`

2. 注释规范
   - 类注释：说明类的用途
   - 方法注释：说明测试目的和步骤
   - 关键代码注释：说明实现逻辑

3. 断言规范
   - 使用 Pytest 断言
   - 断言信息清晰明确

## 常见问题

1. 测试报告生成失败
   - 检查 Outputs 目录权限
   - 确保 allure 命令行工具已安装

2. 测试用例执行失败
   - 检查环境配置
   - 查看日志文件
   - 确认测试数据正确性

## 维护说明
- 定期更新依赖包
- 及时更新测试用例
- 保持代码规范

## 贡献指南
1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 发起 Pull Request

## 版本历史
- v1.0.0: 初始版本
  - 基础框架搭建
  - 核心功能实现
  - 测试报告生成

## 联系方式
- 项目负责人：[姓名]
- 邮箱：[邮箱地址]
- 团队：[团队名称] 