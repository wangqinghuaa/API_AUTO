#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-15 20:12
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm

import unittest
from test_case.test_http_request import TestHttpRequests
from tools.project_path import *


import HTMLTestRunnerNew
from tools.send_email import SendEmail




suite=unittest.TestSuite()
load=unittest.TestLoader()
suite.addTest(load.loadTestsFromTestCase(TestHttpRequests))

with open(test_repect_path, "wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="python单元测试报告",
                                            description="接口登录测试",
                                            tester="er_mao")
    runner.run(suite)


#如果不使用这个发邮件，后面也可以使用jenkins配置自动构建发邮件，看自己选择，当然jenkins更逼格一些
# SendEmail.send_email("wqh18530929470@163.com",test_repect_path)



