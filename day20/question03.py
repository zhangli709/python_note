"""

题目3: 设计一个函数，统计字符串中英文字母和数字各自出现的次数  chr  65-90 97 122 数字到字母   ord  字母到数字

"""


def count_letter_number(string):
    x = 0
    y = 0
    list1 = '0123456789'
    for index, val in enumerate(string):
        if val in list1:
            x += 1
    list2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for val in string:
        if val in list2:
            y += 1
    return y, x


def main():
    print(count_letter_number('a1b2c3d4'))  # (4, 4)
    print(count_letter_number('a123456b'))  # (2, 6)
    print(count_letter_number('123456!!'))  # (0, 6)


if __name__ == '__main__':
    main()
