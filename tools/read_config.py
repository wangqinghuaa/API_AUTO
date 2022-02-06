#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-10 22:22
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : read_config.py
# @Software : PyCharm

import configparser
class Read_Config:
    @staticmethod
    def read_config(file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section,option)

if __name__ == '__main__':
    from tools import project_path
    # print(Read_Config.read_config(project_path.case_config_path,"MODE","mode"))
    # print(Read_Config.read_config(project_path.case_config_path, "DB", "db_config"))
