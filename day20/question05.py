"""

题目5: 设计一个函数，计算字符串中所有数字序列的和

"""
import re


def sum_num_seq(string):
    sum = 0
    list1 = re.findall('\d+', string)
    for val in list1:
        sum += int(val)

    return sum


def main():
    print(sum_num_seq('a1b2c3d4'))  # 10
    print(sum_num_seq('123hello456good789bye'))  # 1368
    print(sum_num_seq('12345678'))  # 12345678
    print(sum_num_seq('abcdefgh'))  # 0


if __name__ == '__main__':
    main()
