"""
集合set :
"""

"""
def main():
    set1 = {1, 1, 2, 2, 3, 3}
    set1.add(4)  # 增加
    print(set1)
    set2 = {1, 3, 5, 7, 9}
    print(set2)
    set3 = set1.intersection(set2)  # 交集 &   set1 & set2
    print(set3)
    set3 = set1.union(set2)  # 并集  |    set1 | set2
    print(set3)
    set3 = set1.difference(set2)  # 差集 = 减去公共部分  -   set1 - set2
    print(set3)
    set3 = set1.symmetric_difference(set2)  # 对称差 = 并集 - 交集  ^  set1 ^ set2
    print(set3)
    for val in set2:
        print(val)
    print(set2.pop())  # 能拿一个，不能保证拿到的是哪个
    print(set2)
    if 3 in set2:
        set2.remove(3)  # 判断，删除元素
    print(set2)
    set4 = {1, 2}
    print(set4.issubset(set1))   # 4是1的子集，  set4 <= set1
    print(set1.issuperset(set4))  # 1包含4.   set1 >= set4


if __name__ == '__main__':
    main()

"""


# 互相转换

"""
def main():
    set1 = {'hello', 'good', 'banana', 'zoo', 'Python', 'hello'}
    print(len(set1))
    x = sorted(set1)
    print(type(x))
    print(x)
    list1 = list(set1)
    print(list1)
    
    
    
if __name__ == '__main__':
    main()
"""

# list 的多重使用, 矩阵，棋盘。*****


def main():
    names = ['关羽', '张飞', '赵云', '马超', '貂蝉']
    subjects = ['语文', '数学', 'Python']
    table = [[0] * len(subjects) for _ in range(len(names))]  # 创建一个5行3列的矩阵。
    for row, name in enumerate(names):
        print('请输入%s的成绩：' % name)
        for col, subject in enumerate(subjects):
            score = int(input('%s:' % subject))   # 输入每个位置的值
            table[row][col] = score  # 将每个位置的值，填进去
    print(table)


if __name__ == '__main__':
    main()

#
# def year(y):
#     y = int(input('请输入年：'))
#     is_True = True
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         is_True = True
#         print('是闰年')
#     else:
#         is_True = False
#         print('不是闰年')
#
#
# def day():
#     year_num = int(input('请输入年份：'))
#     year(year_num)
#     if is_True = True:
#         months = [month for month in range(1, 13)]
#         days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         month_in = input('请输入月份：')
#         for index, month in enumerate(months):
#             if month > len(months):
#                 day =
#
#
#
#
# if __name__ == '__main__':
#    year()


def is_leap_year(y):
    """
    判断是不是闰年，
    :param y: 输入年份
    :return: 闰年返回True, 否则返回False
    """
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False


def which_day(year, month, date):
    """计算传入的日期是这一年的第几天"""
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]  # 调用上面的判断，True返回1， False返回0，以此来选择使用哪个列表。

    total = 0
    for index in range(month - 1):  # 对于输入月之前的每个月，计算天数
        total += days_of_month[index]
    return total + date   # 加上当月的天数，就是这一年的第几天了。


if __name__ == '__main__':
    print(which_day(2018,3,8))


"""
字典 dict
"""


def main():
    dict1 = {'name': '张立', 'age': '34', 'jender': True, 'motto': 'hello world'}
    print(dict1['name'])
    print(dict1['age'])
    print(dict1['jender'])
    dict1['name'] = '王大锤'  # 更新
    print(dict1['name'])
    print(dict1)
    # dict1 +={'tell': '123456788'}
    dict1.update( height=174.5, fav=['吃', '喝']) # 增加元素
    print(dict1.pop('age'))
    print(dict1.popitem())
    # 删除 del
    print(dict1)
    for x in dict1:
        print(x, '--->', dict1[x])  # 查
    # setdefault 返回
    dict1.setdefault('motto', '开心')  # 原来里面有，用原来的，如果未定义，返回我这里定义的。


if __name__ == '__main__':
    main()

# 生成器函数


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


f = fib(20)
print(f)
for val in fib(20):
    print(val)