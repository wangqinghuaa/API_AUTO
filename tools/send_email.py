#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-18 21:39
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : send_email.py
# @Software : PyCharm



import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 邮件发送的用户名和密码  常识：第三方授权码
user="867075698@qq.com"
pwd="rxmkbpuewfodbfah"

now=time.strftime("%Y-%m-%d-%H:%M:%S") #获取时间戳


class SendEmail:

    @staticmethod
    def send_email(email_to, file_path):
        #email_to收件方
        #filepath你要发送邮件的地址
        #如名字所示Multipart就是分多个收件人,通过join将列表转换，以;为间隔的字符串
        msg = MIMEMultipart()
        msg["Subject"] = "二毛的测试报告 "+now
        msg["From"]=user
        msg["To"]=email_to

        #这是文字部分
        part=MIMEText("这是自动化测试结果，请查收！")
        msg.attach(part)


        #加多个附件地址
        # path=["1","2","3","4"]
        # for item in path:
        #     part = MIMEApplication(open(item, "rb").read())
        #     part.add_header("Content-Disposition", "attachment", filename=file_path)
        #     msg.attach(part)

        #这是附件部分=针对一个附件处理
        part=MIMEApplication(open(file_path,"rb").read())
        part.add_header("Content-Disposition","attachment",filename=file_path)
        msg.attach(part)
        s=smtplib.SMTP_SSL("smtp.qq.com",timeout=30) #连接smtp邮件服务器，端口默认是25
        s.login(user,pwd)#登录服务器
        s.sendmail(user,email_to,msg.as_string())#发送邮件：发件方-收件方
        s.close()

if __name__ == '__main__':
    SendEmail.send_email("wqh18530929470@163.com",r"E:\tmp\python11\python0109\test.report.html")