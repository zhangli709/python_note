# from day6 import is_prime
#
# if __name__ == '__main__':
#     for num in range(1, 100):
#         if is_prime == True:
#             print('%d是质数' % num)
#
#
#
# #计算两个数的最大公倍数，最小公约数。
#
#
def lcm(x, y):
    # if x > y:
    #     (x, y) = (y, x)
    '''
    求最小公倍数
    :param x: 任意正整数
    :param y: 任意正整数
    :return: x和y的最小公倍数
    '''
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(y, x * y + 1):
        if i % x == 0 and i % y == 0:
            return i


def gcd(x, y):
    # if x > y:
    #     (x, y) = (y, x)
    #文档注释
    """
    计算最大公约数
    :param x: 任意正整数
    :param y: 任意正整数
    :return: 最大公约数
    """
    #
    (x, y) = (y, x) if x > y else (x, y)
    i = x
    while i > 0:
        if x % i ==0 and y % i == 0: # range(x, 0, -1) 从大到小。
            return i
        i -= 1


if __name__ == '__main__':
    x = int(input('请输入第一个数x='))
    y = int(input('请输入第二个数y='))
    print('最小公倍数：', lcm(x,y))
    print('最大公约数：', gcd(x, y))



#调用函数遇到重名时，调用后面那个函数，后面的把前面的覆盖了， 相当于重新定义了。若想加以区分，请区分名字。

#可变参数的函数


def add(*args): #*args可变参数，个数不确定。
    total = 0
    for value in args:
        total += value
    return total


# if __name__ =="__main__":
#     print(add(1))
#     print(add(1,2))
#
# def add(*args):
#     list1 = []
#     for value in args:
#         list1.append(value)
#     return list1
# if __name__ =="__main__":
#     print(add(1,2,3,4,5,6))
'''  Python一百例2
profit = int(input('请输入总利润：'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for i in range(6):
    if profit > arr[i]:
        r += (profit - arr[i]) * rat[i]
        profit = arr[i]
print(r)
'''
# circle = list(range(1, 31))
# new_circle = circle[::]
#
# new_circle.append(new_circle[0])
# del new_circle[0]
# print(new_circle)

