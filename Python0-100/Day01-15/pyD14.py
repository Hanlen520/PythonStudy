
# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD14.py
@Time    : 2019-06-20  12:44:00
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


# 好像要授权啥的，有点麻烦，不搞了吧 —— 阔以了！！

def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '547636697@qq.com'
    receivers = [ '1225538383@qq.com','547636697@qq.com']
    message = MIMEText('周五快乐~~~~祝彭小帅天天好心情！~！~', 'plain', 'utf-8')
    message['From'] = Header('indeyo', 'utf-8')
    message['To'] = Header('arthinking', 'utf-8')
    message['Subject'] = Header('这是一封。。用python发出的邮件噢~~', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'vvwwpwfznvvrbgag')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

# import urllib.parse
# import http.client
# import json
#
# # 不知道为啥提示账号密码错误，明明是对的。。。。orz...
#
# def main():
#     host  = "106.ihuyi.com"
#     sms_send_uri = "/webservice/sms.php?method=Submit"
#     # 下面的参数需要填入自己注册的账号和对应的密码
#     params = urllib.parse.urlencode({'account': '77239983', 'password': '654321ihuyi', 'content': '今天是2019.6.21，周五啦~我在学习python，真棒！~~', 'mobile': '13686413302', 'format':'json' })
#     print(params)
#     headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
#     conn = http.client.HTTPConnection(host, port=80, timeout=30)
#     conn.request('POST', sms_send_uri, params, headers)
#     response = conn.getresponse()
#     response_str = response.read()
#     jsonstr = response_str.decode('utf-8')
#     print(json.loads(jsonstr))
#     conn.close()



if __name__ == '__main__':
    main()