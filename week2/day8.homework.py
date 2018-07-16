# 设计一个函数，计算传入列表的成绩的平均分，要求去掉一个最高分和一个最低分


def main(n=2):
    grade_list = []
    total = 0
    for _ in range(n):
        grade = int(input('请传入成绩：'))
        grade_list.append(grade)
    # grade_list.sort()
    # grade_list = grade_list[1:-1]
    max_grade = min_grade = grade_list[0]
    for x in grade_list:
        if x > max_grade:
            max_grade = x
        if x < min_grade:
            min_grade = x
    grade_list.remove(max_grade)
    grade_list.remove(min_grade)
    for index, val in enumerate(grade_list):
        total += val
    print('平均分：%.2f' % (total / len(grade_list)))




#  名字加成绩，并输出最高分和最低分


def main():
    names = ['刘备', '张飞', '曹操', '袁绍', '关羽', '赵云', '周瑜']
    scores = []
    for name in names:
        score = input('请输入%s的成绩：' % name)
        scores.append(score)
    min_scores = max_scores = scores[0]
    print(scores)
    name_min = name_max = names[0]
    for s in scores:
        if s > max_scores:
            max_scores = s
            name_max = names[scores.index(s)]
        if s < min_scores:
            min_scores = s
            name_min = names[scores.index(s)]
    print('%s最高分：%s' % (name_max, max_scores))
    print('%s最低分：%s' % (name_min, min_scores))


if __name__ == '__main__':
    main()


# 设计一个函数，从传入的列表中，找出第二大的函数，只能使用一次循环。（元组）tuple（集合）set
# 元组：tuple=(1, 2)  集合： a_set = set() or = {}


def main(n=4):
    list_in = []
    for _ in range(n):
        a = input('请输入你要传入的列表：' )
        list_in.append(a)
    print(list_in)
    list_in.sort()
    a_set = set(list_in)
    list1 = list(a_set)
    # n = len(list1)
    print(list1)
    list1.sort()
    print(list1)
    second_max = list1[-2]
    print('第二大的数为', second_max)


"""
老师评讲
"""
"""
tuple 元组知识。
使用：
1. (1，2，3）叫元组，  1，2，3 也叫元组  （1，）也叫元组
2 stu1 = ('张立', 24， True, '15584548020'
3  不可更改，在时间和空间上都优于列表。
"""

def second_max(x):
    # tuple 元组  不可更改，占的空间小一些。安全一些，能用元组，不用列表。
    """
    输出最大值和第二大的值
    :param x: 输入的列表
    :return: 返回最大值和第二大的值
    """
    (m1, m2) = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif m1 > x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    my_list = [35, 79, 92, 92, 68, 55, 40]
    print(second_max(my_list))




if __name__ == '__main__':
    main()


# if __name__ == '__main__':
#     main(4)