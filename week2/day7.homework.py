# 根据给出的长度，生成相同长度的随机验证码，字母和数字构成的，区分大小写的。A-Z(65-90) a-z(97-122)
# 根据文件名，取出相应的后缀名。
# 生成随机文件名，保证生成的文件名不会和之前的重复。  26个字母加10个数字，生成随机文件名。
# list，   骰子随机数之和，用列表表示。

#我写的！
# list1 = ''
# for x in range(65, 91):
#     list1 += (chr(x))
# for y in range(97, 123):
#     list1 += (chr(y))
# for z in range(0, 10):
#     list1 += 'z'
# print(list1)
#
# from random import randint
#
#
# def main(x):
#     """
#     指定长度的验证码
#     :param x: 指定长度
#     :return: 生成指定长度的验证码。
#     """
#     list2 = ''
#     for i in range(x):
#         list2 += (list1[(randint(0, 61))])
#     return list2
#
#
# if __name__ == '__main__':
#     print(main(4))
#
#
#   #老师评讲!
#
# import random
#
#
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 指定长度
#     :return: 由大小写字母和数字组成的指定长度的随机验证码
#     """
#     all_chars = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, 61)
#         code += all_chars[index]
#     return code
#
#
# if __name__ == '__main__':
#
#     print(generate_code())


# 字符串为空，相当于False. 例子：  i = ''   if i = False


# 根据输入的文件名，输出后缀名。  我写的！
def main(file_name):
    position = file_name.rfind('.')
    if 0 < position < len(file_name)-1:
        suffix_name = file_name[position + 1:]
    else:
        suffix_name = ''
    return suffix_name


if __name__ == '__main__':
    file_name = input('请输入文件名：')
    print(main(file_name))


 #老师讲的！加了是否带点这个功能

def get_suffix(filename, has_dot=False):
    """
    获取文件的后缀名
    :param filename:文件名
    :param has_dot: 是否带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix('.avcc'))
    print(get_suffix('hello.jpg'))
    print(get_suffix('hello.c'))

from random import random, randint
import math


def main(n):
    list1 = []
    for x in range(65, 91):
        list1.append(chr(x))
    for y in range(0, 10):
        list1.append(y)
    print(list1)
    list2 = []
    for i in range(n):
        list2.append(list1[randint(0, 35)])

    return list2


if __name__ == '__main__':
    print(main(11))

# 骰子随机数之和，用list表示   1-(1,6)-6  2-(2,12)-11 3-(3,18)-16 4-(4,24)
from random import random, randint


def main(n, m):
    """
    n个骰子，掷m次的点数和
    :param n: 骰子数
    :param m: 掷的次数
    :return: 点数和
    """
    list = []
    total = 0
    for i in range(n, 6 * n + 1):
        list.append(i)
    print(list)
    for _ in range(m):
        total += randint(n, 6 * n)
    return total


if __name__ == '__main__':
    print(main(6, 4))