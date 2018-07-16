def day_of_week(year01, year02, month):
    if month > 2:
        w = year02 + year02 // 4 + year01 // 4 - 2 * year01 + \
            26 * (month + 1) // 10
        w %= 7
        return w
    else:
        month += 12
        w = year02 + year02 // 4 + year01 // 4 - 2 * year01 + \
            26 * (month + 1) // 10
        w %= 7
        return w


def is_leap_year(year):
    """
判断是否是闰年，返回boolean值
    """
    if year / 4 == 0 and year / 400 != 0:
        return True
    elif year / 100 == 0 and year / 400 == 0:
        return True
    else:
        return False


def days_of_month(month, year):
    if month in [4, 6, 9, 11]:
        month_day = 30
        return month_day
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        month_day = 31
        return month_day
    else:
        if is_leap_year(year):
            month_day = 29
            return month_day
        else:
            month_day = 28
            return month_day


def main():
    year01 = int(input('请输入年份前两位数字'))
    year02 = int(input('请输入年份后两位数字'))
    year = year01 + year02
    month = int(input('请输入月份'))
    print('%10s%10s%10s%10s%10s%10s%10s' % ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'))

    week = day_of_week(year01, year02, month)
    month_day = days_of_month(month,year)
    str_month_day = [x for x in range(1, month_day)]
    str_week = [''] * week
    str_month_day = str_week + str_month_day
    for index, val in enumerate(str_month_day):
        print('%10s' %(val), end='')
        if (index+1) % 7 == 0 and index != 0:
            print('\n')


if __name__ == '__main__':
    main()
