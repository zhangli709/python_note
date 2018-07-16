# 判断是不是回文字符串
# def palindrame(n):
#     if n == n[-1::-1]:
#         print('YES')
#         return True
#     else:
#         print('NO')
#         return False
#
#
# if __name__ == '__main__':
#     n = input('请输入一个字符串：')
#     palindrame(n)


# def palindrame():
#     a = input('请输入一个字符串：')
#     b = len(a)
#     is_palindrame = True
#     while b > 0:
#         if a[0] == a[-1]:
#             a = a[1:-1]
#             b -=2
#         else:
#             print('不是回文字符串')
#             is_palindrame = False
#             break
#     if is_palindrame:
#         print('是回文字符串！')
#     return True
#
#
# if __name__ == '__main__':
#     palindrame()


#  火柴游戏

def main():
    total = 21
    while total > 0:
        i_take = int(input('请输入你拿的火柴数；'))
        if 1 <= i_take <= 4 and i_take <= total:
            total -= i_take
            print('还剩下%d' % total)
        com = int(5-i_take)
    return


if __name__ == '__main__':
    main()


