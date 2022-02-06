#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-15 21:26
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : project_path.py
# @Software : PyCharm

import os

'''专门读取路径的值'''

#获取顶级目录
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)


#测试用例的路径
test_case_path=os.path.join(project_path,"test_data","tests.xlsx")
# print(test_case_path)

#测试报告的路径
test_repect_path=os.path.join(project_path,"test_result","http_report","test_api.html")
# print(test_repect_path)


#配置文件的路径
case_config_path=os.path.join(project_path,"conf","case.config")
# print(case_config_path)

#配置文件2路径
mysql_config_path=os.path.join(project_path,"conf","mysql.config")

#日志文件的路径
log_path=os.path.join(project_path,"test_result","log","test_api.txt")

