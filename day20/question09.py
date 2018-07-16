"""

题目9: 设计一个函数，传入两个代表日期的字符串，如“2018-2-26”、“2017-12-12”，计算两个日期相差多少天

"""
import re


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
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]  # 调用上面的判断，True返回1， False返回0，以此来选择使用哪个列表。

    total = 0
    for index in range(month - 1):  # 对于输入月之前的每个月，计算天数
        total += days_of_month[index]
    return total + date  # 加上当月的天数，就是这一年的第几天了。


def diff_days(date1, date2):
    list1 = re.findall('\d+', date1)
    list2 = re.findall('\d+', date2)
    year1 = int(list1[0])
    month1 = int(list1[1])
    date1 = int(list1[2])
    year2 = int(list2[0])
    month2 = int(list2[1])
    date2 = int(list2[2])
    num1 = which_day(year1, month1, date1)
    num2 = which_day(year2, month2, date2)
    if is_leap_year(year1):
        surplus = 366 - num1 + 1
    else:
        surplus = 365 - num1 + 1
    return surplus + num2


def main():
    print(diff_days('2017-12-12', '2018-2-26'))  # 76
    print(diff_days('1979-12-31', '1980-11-28'))  # 333


if __name__ == '__main__':
    main()
