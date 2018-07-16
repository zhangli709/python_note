# from random import random, randint,randrange
#
#
# def main():
#     red_balls = [x for x in range(1, 34)]
#     blue_balls = [y for y in range(1, 17)]
#     red_ball6 = []
#     for x in range(6):
#         index = randrange(len(red_balls))
#         red_ball6.append(red_balls[index])
#         del red_balls[index]
        
#     red_ball6.append(randrange(blue_balls)
#     print(red_ball6)
#
#
#
# if __name__ == '__main__':
#     main()

from random import randrange, randint


def display(balls):
    """
    美化输出球的页面
    :param balls: 输入的列表
    :return: 优化过的列表
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
             print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    6个红球的随机数（1-33）和1个蓝球的随机数（1-16）
    :return: 6个红球和一个蓝球的随机组合
    """
    red_balls = list(range(1, 34))
    select_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        select_balls.append(red_balls[index])
        del red_balls[index]
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls


def main():
    """
    注数，及返回值
    :return: 多少注的双色球随机数
    """
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()