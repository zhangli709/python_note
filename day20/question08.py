"""

题目8: 设计一个函数，统计一个字符串中出现频率最高的字符及其出现次数

"""


def find_most_freq(string):
    max_number = 0
    my_list = []
    my_dict = {}
    for index, val in enumerate(string):
        if string.count(val) > max_number:
            max_number = string.count(val)
            my_dict = {val: max_number}
        elif string.count(val) == max_number:
            my_dict[val] = max_number
    for val, key in my_dict.items():
        my_list.append(val)
    return my_list, max_number


def main():
    print(find_most_freq('aabbaaccbb'))  # (['a', 'b'], 4)
    print(find_most_freq('hello, world!'))  # (['l'], 3)
    print(find_most_freq('a1bb2ccc3aa'))  # (['a', 'c'], 3)


if __name__ == '__main__':
    main()
