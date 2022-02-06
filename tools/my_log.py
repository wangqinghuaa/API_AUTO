#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-16 18:00
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : my_log.py
# @Software : PyCharm




import logging
from tools import project_path


class My_Logging:

    def my_log(self,msg,level):

        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger("python")

        #设定级别
        my_logger.setLevel("DEBUG")

        #设定日志输出方式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 创建我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("ERROR")
        ch.setFormatter(formatter)

        fh = logging.FileHandler(project_path.log_path, encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        #两者对接-指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level=="WARNING":
            my_logger.warning(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        elif level=="CRITICAL":
            my_logger.critical(msg)
        #关闭日志收集-关闭渠道-不然会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self.my_log(msg,"DEBUG")
    def info(self,msg):
        self.my_log(msg,"INFO")
    def error(self,msg):
        self.my_log(msg,"ERROR")
    def critical(self,msg):
        self.my_log(msg,"CRITICAL")
    def warning(self,msg):
       self.my_log(msg,"WARNING")
if __name__ == '__main__':

    my_logger=My_Logging()
    my_logger.debug("可行吗")
    my_logger.info("可行")