# #打印三角形图案
# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*',end='')
#     print()
#  row = int(input('请输入行数：'))
# for i in range(row):
#     print()
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()
# for i in range(row):
#     for _ in range(row - i - 1):
#         print('   ', end ='')
#     for _ in range(2 *i + 1):
#         print(' * ',end ='')
#     print()


"""

输入M N ，计算C（m,n)
"""


# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

'''函数
我们可以把程序中相对独立的功能模块抽取出来
这样的好处可以减少重复代码的编写
将来可以重复使用这些功能模块
Python 中的函数就是代表了这样的功能模块
命名：age_of_student(官方)  或 ageOfStudent（大部分人习惯用法：驼峰命名法）
调用：函数名（参数）。
二元运算符之间放空格。tips:参数里赋值时，等号两边不加空格。 例如：def f(x=2).
'''


# y = x !定义求阶乘这个函数，将求阶乘这个功能抽取出来，放到函数中。


# def f(x):
#     """
#     求函数x的阶乘
#     :param x: 任意正整数
#     :return: x的阶乘
#     """
#     y = 1
#     for z in range(1, x + 1):
#         y *= z
#     return y
#
#
# if __name__ == '__main__':
#     m = int(input('m = '))
#     n = int(input('n = '))
#     # 当需要计算阶乘的时候，不用再写循环，而是直接调用已经定义好的函数就可以了。
#     print(f(m) // f(n) // f(m - n))


# def f(x):
#     y = 1
#     for a in range(1, x + 1):
#         y *= a
#     return y
#
#
# n = int(input('n = '))
# m = int(input('m = '))
# print(f(n) // f(m) // f(n - m))

#  Craps游戏函数改进版

from random import randint


# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# # 改名字，选中要修改的名字，按中shift + F6
# from random import randint
# money = 1000
# while money >0:
#     print('玩家总资产：%d' % money)
#     while True:
#         debt = int(input('清下注：'))
#         if 0 < debt <= money:
#             break
#     go_on = False
#
#     print('玩家摇出了%d' % roll_dice())
#     if roll_dice() == 7 or roll_dice() == 11:
#         print('玩家胜')
#         money += debt
#     elif roll_dice() == 2 or roll_dice() == 3 or roll_dice() == 12:
#         print('玩家输')
#         money -= debt
#     else:
#         go_on = True
#     while go_on:
#         roll_dice()
#         print('玩家摇出了%d' % roll_dice())
#         if roll_dice() == roll_dice():
#             print('玩家胜!')
#             money += debt
#             go_on = False
#         elif roll_dice() == 7:
#             print('玩家输!')
#             money -= debt
#             go_on = False
# print('你已经破产！')

#  判断是不是质数

from math import sqrt
def is_prime(num):

    for factor in range(2,int(sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return num !=1 and True or False
 # 通过下面的if条件，可以在导入模块时不去执行下面的代码。
# ctrl + 鼠标左键 可以查找解释定义。

if __name__ == '__main__':
    num = int(input('请输入一个数判断是不是质数：'))
    print(is_prime(num))


'''
函数：
def 函数名（参数，即自变量）:
    
    （这里写文档注释，很重要）
    
    方法
    return 应变量

'''
'''
import 模块 (as  别名)
使用：
   模块名.函数
'''
# a = 'abcdefg'  # input('请输入字符串')
# print(a[-1::-1])
#  字符串倒过来的做法：[-1::-1]





