#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-15 20:06
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_http_request.py
# @Software : PyCharm


import unittest
from tools.http_request import Http_request
from tools.get_data import GgtData
from ddt import ddt,data
from tools.do_excel import Do_Excel
from tools.project_path import *
from tools.my_log import My_Logging
my_log=My_Logging()#创建一个实例

test_data=Do_Excel().get_data(test_case_path)

@ddt
class TestHttpRequests(unittest.TestCase):

    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        res = Http_request().http_request(item["url"], eval(item["data"]), item["method"],getattr(GgtData,"COOKIES"))

        if res.cookies:  #有cookies的话，就更新cookies
            setattr(GgtData,"COOKIES",res.cookies)
        try:
            # 不加断言全部都是OK，加了断言会用实际值和期望值做对比，如果不一致会报错:F
            self.assertEqual(item["expected"], res.json()["retcode"])
            TestResult="PASS" #成功的
        except Exception as e:
            TestResult = "Failed"  # 失败的
            my_log.info("执行用例出错：{0}".format(e))
            raise e
        finally: #不管对错都会执行，保存到excle里面
            Do_Excel().write_back(test_case_path, item["sheet_name"], item["case_id"]+1, str(res.json()),TestResult)
            my_log.error("获取的结果是：{0}".format(res.json()))
    def tearDown(self):
        pass
