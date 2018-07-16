# python 自动发邮件，短信。
# MIME -- Multipurpose Internet Mail Extension 多用途因特网邮件扩展。
# SPM 垃圾邮件，不让发送。
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = SMTP('smtp.163.com')  # 使用的协议
    sender.login('zhangli9479@163.com', 'zl121525')  # 连接登陆
    message = MIMEMultipart()
    message['Subject'] = '请查收'
    text_msg = MIMEText('附件中有本月重要数据，记得查收', 'plain', 'utf-8')  # 邮件内容
    message.attach(text_msg)
    #message['Subject'] = ''  # 邮件名
    #sender.sendmail('zhangli9479@163.com', ['1261061345@qq.com'], message.as_string())  # 发送
    att2 = MIMEText(open('mm.jpg', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att2["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att2)
    sender.sendmail('zhangli9479@163.com', ['1261061345@qq.com'], message.as_string())
    print('发送成功')


if __name__ == '__main__':
    main()