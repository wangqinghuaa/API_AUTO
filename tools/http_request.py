#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 11:23
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : http_request.py
# @Software : PyCharm


import requests
from tools.my_log import My_Logging
my_log=My_Logging()#创建一个实例


class Http_request:


    def http_request(self,url,data,method,cookie=None):
        try:
            if method.lower()=='get':
                res = requests.get(url,data,cookies=cookie)
            #艾已付
            elif method.lower()=='post':
                res = requests.post(url, data, cookies=cookie)
            elif method.lower()=='delete':
                res = requests.delete(url, cookies=cookie)
            elif method.lower()=='put':
                res = requests.put(url, data, cookies=cookie)
            #艾欧斯
            else:
                my_log.info("输入的请求方法不对")
        #一颗赛普特  一颗赛普深
        except Exception as e:

            my_log.error("请求报错了：{}".format(e))
            raise e  #瑞z
        return res  #返回消息实体



if __name__ == '__main__':
    url = "http://localhost:8066/api/mgr/loginReq"
    data = {"username": "auto", "password": "sdfsdfsdf"}
    res = Http_request().http_request(url,data,"post")
    print("登录的结果是:",res.json())
    print("登录的cookies是{0}".format(res.cookies))

    list_url = "http://localhost:8066/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
    ress = Http_request().http_request(list_url,{},'get',res.cookies)
    print("列出的课程是:",ress.json())