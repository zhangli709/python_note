"""

题目2: 设计一个函数，生成指定长度的验证码（由数字和大小写英文字母构成的随机字符串）

"""

from random import randrange


def generate_code(length=4):
    sum = ""
    string = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for _ in range(length):
        sum += (string[randrange(62)])
    return sum


def main():
    for _ in range(10):
        print(generate_code())


if __name__ == '__main__':
    main()
