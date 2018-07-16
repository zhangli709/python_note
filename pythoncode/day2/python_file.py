Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import getpass
username = input('请输入用户名：')
password = getpass.getpass('请输入密码：')
if username =='admin' and password == '123456':
    print('欢迎使用本系统.')
else:
    print('用户名或密码错误！')
    
