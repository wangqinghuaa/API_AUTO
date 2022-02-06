#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-17 23:29
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : do_mysql.py
# @Software : PyCharm


import mysql.connector
from tools import project_path
from tools.read_config import Read_Config

class DoMysql:

    def do_mysql(self,query_sql,state="all"):  #利用类从配置文件读取info
        db_config=eval(Read_Config().read_config(project_path.case_config_path,"DB","db_config"))
        cnn=mysql.connector.connect(**db_config)

        cursor=cnn.cursor()
        cursor.execute(query_sql)

        if state==1:
            res=cursor.fetchone()
        else:
            res=cursor.fetchall()

        cursor.close()
        cnn.close()
        return res

if __name__ == '__main__':
    slect_sql = 'select max(score) from students where score like "9%"'
    #传1
    res=DoMysql().do_mysql(slect_sql,1)
    print(res[0])

    # #不传1
    # res=DoMysql().do_mysql(slect_sql)
    # print(res[0][0])
