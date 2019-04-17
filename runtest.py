#coding=utf-8
#author='Shichao-Dong'

import time,os
import unittest
# import testsuites
import HTMLTestRunner
import smtplib
import datetime
from public.readConfig import Readconfig
from public.Sendemail import Email
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart

# from testcase.CmTest import Cm


PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

# def testsuit():
suite = unittest.TestLoader().discover('testcase')

# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

now=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
dirpath = PATH("./results/商城app365-")

filename=dirpath + now +'result.html'
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'天琨鲜生app test result',description=u'自动化测试结果')
    # runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()

#
# def send_email():
#     #定义发件箱
#     conf = Readconfig()
#     smtpsever = conf.getemailValue('smtpsever')
#     user = conf.getemailValue('user')
#     password = conf.getemailValue('password')
#     sender = conf.getemailValue('sender')
#     receiver = conf.getemailValue('receiver')
#
#     sendemail = Email()
#     msg=sendemail.email()
#
#     #发送邮件
#     smtp=smtplib.SMTP()
#     smtp.connect(smtpsever)
#     smtp.login(user,password)
#     smtp.sendmail(sender,receiver.split(','),msg.as_string())
#     smtp.quit()
#     print(u'邮件发送成功')
#
# if __name__ == "__main__":
#
#     # runner=unittest.TextTestRunner()
#     # runner.run(suite)
#
#     testsuit()
#     # send_email()