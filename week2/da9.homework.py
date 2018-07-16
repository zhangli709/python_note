# 杨辉三角
# 螺旋矩阵。
def replaceSpace():
    # list1 = [1]
    # list2 = [1, 1]
    # list3 = [1, 2, 1]
    my_list =[]
    for i in range(10):
        for index in range(i + 1):
            my_list[i][index]



if __name__ == '__main__':
    print(replaceSpace())


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0]+a, a+[0])]



if __name__ == '__main__':
    n = 0
    for t in triangles():
        print(t)
        n = n+1
        if n == 10:
            break