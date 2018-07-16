# 把可能出现状况的代码，放到try中，保护执行。
# except 如果try中出现了状况，那么在此处执行，可以写多个用于处理各种异常情况。
# 如果没有出现状况，那么把无风险的文件放到else中执行
# finally  不管程序正常还是异常，在这里都会执行，所以这里放释放外部资源的操作。

from math import sqrt


def is_prime(n):
    assert n > 0
    for val in range(1, int(sqrt(n)) + 1):
        if n % val == 0:
            return False
    return True if n != 0 else False


def main():
    try:
        for n in range(2, 10000):
            if is_prime(n):
                if 0 < n < 100:
                    with open('../abcd/hello.txt', 'w') as n1:
                        n1.write(str(n))
                elif 100 <= n < 1000:
                    with open('../efg/hello', 'w') as n2:
                        n2.write(str(n))
                elif 1000 <= n < 10000:
                    with open('hello.txt', 'w') as n3:
                        n3.write(str(n))

        # 此处是最好的释放文件的位置，因为此处总是能执行到。
    except FileNotFoundError:
        print('找不到文件')
    #finally:

    print('执行完成')



if __name__ == '__main__':
    main()