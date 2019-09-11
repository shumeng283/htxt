# Author :lixinhao
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from econtract_login import (ss,login)
from Var import  global_var
import time

class SendMail():
    def send_mail(self,subject,content=None):
        #socks.set_default_proxy(socks.HTTP, addr='proxy1.bj.petrochina', port=8080)
        #socket.socket = socks.socksocket
        msg_from = 'shumeng283@163.com'  # 发送方邮箱
        passwd = 's123456'  # 填入发送方邮箱的授权码
        msg_to = ['shumeng@hffss.com','wangyc@hffss.com']  # 收件人邮箱
        #subject = 'HSE2.0海外子系统-首页预警'  # 主题
        #content = '11'  # 正文
        msg = MIMEMultipart(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = ','.join(msg_to)
        msg.attach(MIMEText('接口自动化测试报告'))
        att1 = MIMEApplication(open('C:/Users/lixh/Desktop/res10.html', 'rb').read())
        att1.add_header(
                'Content-Disposition',
                'attachment', filename=('gbk', '', '测试报告.html'))
        msg.attach(att1)
        try:
            s = smtplib.SMTP_SSL("smtp.163.com", 465)  # 邮件服务器及端口号
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")
        except smtplib.SMTPException:
            print("发送失败")

if __name__ == '__main__':
    test_dir = 'D:/test_htxt'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='htxt*.py')#添加所有用例
    runner = unittest.TextTestRunner()
    with open("C:/Users/lixh/Desktop/res10.html",'wb') as fr:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="接口测试报告",description="测试用例结果",tester=u"舒萌")
        # 生成执行用例的对象
        runner.run(discover)
    fr.close()
    time.sleep(1)
    SendMail().send_mail('测试')