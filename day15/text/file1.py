"""文件的读写"""
"""red , redline, readlines"""
#  ../ 表示上一级， ../../表示上两级
#  异常机制， 处理程序在运行过程中出现的意外状况的手段
#  因为不是所有的问题都能够写程序时就能发现的。

#  打开文件  判断大小  分配内存  读取文件 关闭文件

import time


def main():
    # stream = open('hello.txt', 'r', encoding='utf-8')
    # content = stream.read()
    # print(content)
    # stream.close()
    #
    # fs = open('hello.txt', 'r', encoding='utf-8')
    # content = fs.read()
    # print(content)
    # fs.close()
    # try:  # 把可能出现状况的代码保护起来，执行最小惊讶原则。
    #     with open('../abcd/hello.txt', 'r', encoding='utf-8') as fs:  # 标准写法。 打开文件名，采取操作（r,w,a),(记住！)
    #         mylist = fs.readlines()
    #         for line in mylist:
    #             print(line, end='')
    #             time.sleep(0.5)
    # except FileExistsError:
    #     print('指定的文件无法打开')
    # print()
    # print('程序执行结束！')
    try:
        with open('abcd/hello.txt', 'r', encoding='utf-8') as fs:
            mylist = fs.readlines()
            for line in mylist:
                print(line, end=' ')
                time.sleep(0.3)
    except FileNotFoundError:
        print('无法打开')
    except IOError:
        print('读写错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()

