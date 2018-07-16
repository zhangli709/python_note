"""

题目4: 设计一个函数，判断传入的整数列表（要求元素个数大于2个）中的元素能否构成等差数列

"""


def is_arithmetic_series(num_list):
    new_list = sorted(num_list)
    for index in range(1, len(new_list)-1):
        if new_list[index] *2 != new_list[index-1] + new_list[index+1]:
            return False
    return True


def main():
    list1 = [1, 3, 5, 7, 9]
    list2 = [100, 500, 200, 400, 300]
    list3 = [1, 2, 3, 5, 6, 7]
    print(is_arithmetic_series(list1))  # True
    print(is_arithmetic_series(list2))  # True
    print(is_arithmetic_series(list3))  # False


if __name__ == '__main__':
    main()

#######################################
