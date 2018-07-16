a = 100
#  在函数外面，全局变量  global variable
#  减少全局变量的使用，尽量使用局部变量。 迪米特法则；不要和陌生人讲话，尽量不要让模块之间发生关联。
#  Python搜索一个变量的方式是从局部作用域到嵌套作用域再到全局作用域，local > enclose > global > built-in (l e g b)
#  如果想改变搜索范围，可以使用global和nonlocal关键字。


# def foo():
#     #  函数内的局部变量，离开foo函数时无法访问的。 local variable
#     global a
#     #  提升权限，变为全局变量，可以直接修改，重新定义申明的变量。
#     a = 200
#     print(a)
#     b = 'good'
#
#     def bar():
#         nonlocal b
#         #  非局部作用域。
#         b = 'hello'
#         print(b)
#         print(a)
#     bar()
#     print(b)
#
#
# foo()
# print(a)
#  写的每一个程序都写到函数里去
"""
定义一个函数，再来写代码。
写完之后，再用一个if __name__ =='__main__':
来执行。
"""


# def palindrame():
#     str_word = input('请输入一个字符串：')
#     n = len(str_word)
#     is_palindrame = True
#     while n >= 0:
#         if str_word[0] == str_word[-1]:
#             str_word = str_word[1:-1]
#             n -= 2
#         else:
#             print('不是回文字符！')
#             is_palindrame = False
#             break
#     if is_palindrame:
#         print('是回文字符')
#
#
# if __name__ == '__main__':
#     palindrame()

#
# def main():
#     total = 21
#     while total > 0:
#         print('总共还有%d根火柴' % total)
#         while True:
#             num = int(input('拿几根火柴：'))
#             if 1 <= num <= 4 and num <= total:
#                 break
#         total -= num
#         if total > 0:
#             print('计算机拿走了%d根火柴' %(5-num))
#             total -= 5 - num
#     print('你拿到了最后一根火柴，你输了！')
#
#
# if __name__ == '__main__':
#     main()

#  21根火柴游戏
from random import randint


# def main():
#     total = 21
#     while total > 0:
#         print('还剩下%d根火柴' % total)
#         while True:
#             num = int(input('请输入你要拿的火柴数：'))
#             if 1 <= num <= 4 and num <= total:
#                 break
#         total -= num
#         print('你拿完之后还剩%d' % total)
#         if total > 0:
#             com = randint(1,min(4,total))
#             print('电脑拿了%d根火柴' % com)
#             total -= com
#             if total == 0:
#                 print('电脑拿走了最后一根火柴，电脑输了！')
#                 break
#         if total == 0:
#             print('你拿走了最后一根火柴，你输了1')
#
#
# if __name__ == '__main__':
#     main()


#  内置函数 built-in
# print(print)
# print(int)
# print(chr)

#  函数自己调用自己 -- 递归函数。 call-self
#  foo bar 相当于举个栗子  foo - fuck up   bar - beyond all recognition


#  n! = n * (n - 1)
# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * f(n - 1)
#  f(5) = 5 * f(4)
#  f(4) = 4 * f(3)
#  f(3) = 3 * f(2)
#  f(2) = 2 * f(1)
#  f(1) = 1   再依次返回值。
#  递归还是循环。


# if __name__ == '__main__':
#     print(f(1))


#  保存现场 - 保存，恢复现场
#  在进入函数调用之前，要保存当前的执行现场，函数的执行现场是保存在一种称为栈（stack)的内存空间上。
#  stack 栈- 先进后出（FILO)的存储结构，栈就几兆的空间，计算速度很快。例子 ，安卓系统的返回系统--栈结构。

#  短除法求最大公约数
# def gcd(x, y):
#     """
#     短除法求最大公约数
#     :param x: 任意正整数x
#     :param y: 任意正整数y
#     :return: 返回x和y的最大公约数
#     """
#     if x > y:
#         return gcd(y, x)
#     elif y % x == 0:
#         return x
#     else:
#         return gcd(y % x, x)
#
#
# if __name__ == '__main__':
#     print(gcd(12, 27))


#  1到100递归求和，
#  十级楼梯，走完十级台阶有几种走法。一到三，


# def sum_(num):
#     if num == 1:
#         return 1
#     return sum_(num - 1) + num
#
#
# if __name__ == '__main__':
#     print(sum_(100))

# from random import randint
#
#
# def way(num):
#     while num > 0:
#         print(num)
#         return way(num-randint(1,min(3, num)))
#         if num == 0:
#             return
#
#
# if __name__ == '__main__':
#     way(10)

#  递归调用
#  1.收敛条件 - 让递归在有限的次数内完成或者进行回溯
#  如果递归无法在有限的次数内收敛，就有可能导致RecursionError
#  2.递归公式

def walk(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return walk(n-1) + walk(n-2) + walk(n-3)


if __name__ == '__main__':
    print(walk(25))


# kg 10**3   Kg 2**10 == 1024  100Mbps   8bit == 1 Byte 1024Byte == 1 KB  