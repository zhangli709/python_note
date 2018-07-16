"""

题目7: 设计“跳一跳”游戏的计分函数，“跳一跳”游戏中黑色小人从一个方块跳到另一个方块上会获得1分，
如果跳到方块的中心点上会获得2分，连续跳到中心点会依次获得2分、4分、6分、……。该函数传入一个列表，
列表中用布尔值True或False表示是否跳到方块的中心点，函数返回最后获得的分数

"""


def calc_score(jump_list):
    """人类自然语言，转为机器语言"""
    count = 0
    score = 0
    for val in jump_list:
        if val == True:
            count += 1
            score += count * 2
        elif val == False:
            count = 0
            score += 1
    return score


def main():
    list1 = [True, False, False, True, True, True]
    list2 = [True, True, True, True, False, True, True]
    list3 = [False, False, True, True, True, True, True, False]
    print(calc_score(list1))  # 16
    print(calc_score(list2))  # 27
    print(calc_score(list3))  # 33


if __name__ == '__main__':
    main()

##############
