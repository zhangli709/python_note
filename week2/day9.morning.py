# 约瑟夫环问题
# from random import randint
#
#
# def main():
#     circle = list(range(1, 31))
#     new_circle = circle[::]
#     while len(new_circle) > 15:
#         for i in randint(1, 9):
#             if i < 9:
#                 new_circle.append(new_circle[0])
#                 del new_circle[0]
#             elif i == 9:
#                 del new_circle[0]
#     print(new_circle)


def main():
    """
    约瑟夫环问题，
    :return: 基督徒和非基督徒站的顺序。
    """
    persons = [True] * 30  # 30个人活着，用True表示。
    counter = 0  # 死的人。
    index = 0    # 下标
    number = 0   # 报数
    while counter < 15:  # 死的人小于15继续进行
        if persons[index]:  # 活着的人报数
            number += 1
            if number == 9:     # 报数为9的人被杀死
                persons[index] = False
                counter += 1    # 死的人加一
                number = 0  # 重新报数
        index += 1  # 下标一直增加，
        index %= 30  # 超过30开始循环，又回到0开始，
    for person in persons:  # 在这些人中，死了的标记为非，没死的标记为基
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()


