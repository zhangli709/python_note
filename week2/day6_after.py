# import test as test   # as  用于取别名，取一个简短一点的名字。
# import math
# if __name__ =="__main__":
#     print(math.gcd(5, 7))  #gcd最大公约数。
#     print(test.lcm(22, 15)) #ctrl + q 可以查看这个函数的文档注释。
#     print(test.gcd(5, 7))

# 1整数，判断是不是回文数，正着读，倒着读都一样。
# 2.回文质数


# from math import sqrt
# def is_prime(num):
#
#     for factor in range(2,int(sqrt(num)) + 1):
#         if num  % factor == 0:
#             return False
#     return num !=1 and True or False
# # 通过下面的if条件，可以在导入模块时不去执行下面的代码。
# # ctrl + 鼠标左键 可以查找解释定义。
#
#
#
#
# # if __name__ =='__main__':
# #     num = int(input('请输入一个需要判断的数：'))
# #     print('回文数：', palindromic_number(num))
# #     print('质数：', prime_number(num))
#
#
#
# def is_palindrome(num):
#     '''
#     判断是不是回文数
#     :param num: 非负整数
#     :return: 是回文数返回True,不是回文数返回Flase.
#     '''
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return num == total
# #and和or运算符都是带短路功能的运算符
# #如果and左边的表达式是Flase,那么右边的表达式被短路
# #如果or左边的表达式是True,那么右边的表达式被短路
# #所以左右两边的表达式放置的顺序可能会对执行效率产生明显的影响。
# if __name__ == "__main__":
#     num = int(input('请输入一个数：'))
#     print(is_palindrome(num))
#     if is_palindrome(num) and prime_number(num):
#         print('%是回文质数' % num)
#     else:
#         print('%f不是回文质数' % num)


#homework  21根火柴的游戏，谁拿到最后一根，谁就输。每次拿的范围[1,4].保证计算机获胜。
#字符串回文。

from random import randint
def game_match():
    total = 21
    while True:
        my_number = int(input('请输入你拿的火柴数：'))
        if 1 <= my_number <= 4:
            com_number = 5 - my_number
            total -= 5
            print('电脑拿完还有多少根', total)
        if total == 1:
            print('你输了')
            break
        else:
            print('请输入正确的火柴数!')


if __name__ == '__main__':
    game_match()

# str_word = input('请输入一个字符串：')
# n = len(str_word)
# is_palindrame = True
# while n >= 0:
#     if str_word[0] == str_word[-1]:
#         str_word = str_word[1:-1]
#         n -= 2
#     else:
#         print('不是回文字符！')
#         is_palindrame = False
# if is_palindrame:
#     print('是回文字符')