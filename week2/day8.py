# 作业评讲，列表做掷骰子的次数。
from random import random, randint
# 有了列表容器，我们可以使用1个变量来保存多个数据
# 更为重要的是，我们可以使用循环对列表中保存的数据进行操作。


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def main():
    """
    一个骰子掷6万次，每个面出现的次数
    :return: 每个面出现的次数
    """

    f = [0] * 11
    for _ in range(60000):
        face = roll_dice()
        f[face - 2] += 1

    for index, val in enumerate(f):
        print('%d点摇出的次数%d为%.2f%%' % (index + 2, val, f[index] / 600))
    # 直接通过for-in循环对列表进行遍历。
    for counter in f:
        print(counter)


if __name__ == '__main__':
    main()


def main():
    f = [100, 200, 500]
    # print(f[0], f[1], f[2])
    # for val in f:
    #     val += 10
    #     print(val)
    # print(f)
    # # 遍历容器最好的做法！！！！！ 既有下标，又有值。
    # for index, val in enumerate(f):
    #     print(index, ':', val)
    # CRUD操作Create Read Update Delete
    f.append(1)  # 追加
    f.insert(1, 1)  # 插入
    # f.remove(500)   # 知道值，移除列表中的值，移除遇到的第一个值。如果没有就报错
    if 1 in f:
        f.remove(1)  # 上面的加强版，不知道值和位置
    # f.clear()  # 全部清除
    del f[2]   # 直到位置，直接删除指定位置的元素
    print(f.index(100, 0, 5))  # 知道元素，找指定范围内元素的位置。
    f.pop()   # 不带入参数，默认删除最后一个值。

    print(f)



if __name__ == '__main__':
    main()


# [1,1,2,3,5,8,13,21,...] 叫fibonacci序列。黄金分割！

# def main(n):
#     f = [1, 1]
#     for i in range(2, n):
#         val = f[i - 1] + f[i-2]
#         f.append(val)
#         print(f)
#     f2 = f[18:]
#     print(f2)
#     print(f2[0]/f2[1])
#     f3 = f[::-1]  # 反转容器
#     f.reverse()  # 反转
#     print(f)
#     print (f3)
#
#
# if __name__ == '__main__':
#     main(20)


def main():
    f = ['a', 'b', 'c', 'd', 'f']
    f2 = sorted(f, reverse=True)
    # Python 默认的 排序方法，都是排升序（从小到大）
    # 如果希望排列成降序，（从大到小），可以通过reverse参数来指定，
    # Python 中的函数，几乎都是没有副作用的。调用函数之后，不会影响传入的参数。
    print(f)
    print(f2)
    f.sort(reverse=True)  # 改这个列表本身。，调用它本身的方法。
    print(f)


if __name__ == '__main__':
    main()



#  列表中的数字，找最大值，最小值，找平均值。
#  按单词的长短来排序。

