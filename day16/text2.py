# def is_vaild_username(username):
#     """判断用户名是否有效，字母数字下划线构成，且长度在6-20个字符"""
#     if 6 <= len(username) <= 20:
#         for ch in username:
#             if not ('0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or ch == '_'):
#                 return False
#         return True
#     return False
#
#
# def main():
#     print(is_vaild_username('asdgg1'))
#
#
# if __name__ == '__main__':
#     main()


## 正则表达式 -- 工具 -- 定义字符串的匹配模式
# \w{6, 20}
# \w 一个字母或数字或下划线  \d一个数字   .除换行符以外的任意字符   *任意字符   +至少一个字符
# ？表示0或1个字符  \s 任意的空白符 {n}表示n个字符   {n,m}表示n到m个字符。

# \大写字母， 上面的意思取相反。[^adb] 除了这个里面的任意字符


# [0-9a-zA-Z\_]  可以匹配一个数字、字母或下划线
# [0-9a-zA-Z\_]+  可以匹配至少一个数字、字母或下划线
# [0-9a-zA-Z\_]*  可以匹配任意个数字、字母或下划线
# [a-zA-Z\_][0-9a-zA-Z\_]*  匹配由字母下划线开头，后接任意个由字母数字下划线组成的字符
# A|B A或B
# ^ 表示行的开头 ^\d 表示必须由数字开头
# $ 表示行的结束  \d 表示必须以数字结束


# re -- regulary


import re
def main():
    username = 'jackfrued'
    if re.match(r'^\w{6,20}$', username):
        # 如果匹配成功，返回True, 失败，返回None
        # search 也行
        print('匹配成功')
    else:
        print('无效的用户名')
    m = re.match(r'^\w{6,20}$', username)
    print(m.span())
    print(m.group())


if __name__ == '__main__':
    main()



# 用户名和qq号的验证

# import re
# def main():
#     username = input('请输入用户名：')
#     qq_num = input('请输入QQ号')
#     pattern1 = re.compile(r'^[1,9]\d{4,11}$')  # 创建正则表达式, 两种写法
#     if pattern1.match(qq_num):
#         print('qq号匹配成功')
#         if re.match(r'^[0-9A-Za-z]{6,20}$', username):
#             print('用户名匹配成功')
#         else:
#             print('用户名错误')
#     else:
#         print('QQ号错误')
#
#
# if __name__ == '__main__':
#    main()