# 自动发短信。 互亿
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = SMTP('smtp.126.com')
    sender.login('cd_ios_1605@126.com', '1qaz2wsx')
    message = MIMEMultipart()
    message['From'] = '骆昊'
    message['To'] = '瓜西西'
    message['Cc'] = 'shuling@1000phone.com'
    message['Subject'] = '请查收附件中的数据'
    text_msg = MIMEText('附件中有本月关键数据请查收!', 'plain', 'utf-8')
    message.attach(text_msg)

    att2 = MIMEText(open('hello.xlsx', 'rb').read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/vnd.ms-excel'
    att2['Content-Disposition'] = 'attachment; filename=foo.xlsx'
    message.attach(att2)

    sender.sendmail('cd_ios_1605@126.com',
                    ['957658@qq.com', 'jackfrued@126.com'],
                    message.as_string())

    print('发送完成!')


if __name__ == '__main__':
    main()
