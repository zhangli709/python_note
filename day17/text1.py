# 多线程，多进程

# 进程： 操作系统分配内存的基本单位， 进程之间的通信时相互隔离的，如果要相互交换数据，
#       要使用一个特殊的机制。
# 线程： 一个进程可以划分为多个线程 ，线程是进程的执行单元，也是操作系统分配cpu的基本单元。

# 多线程，是为了多的被CPU所启动。
# 多线程和多进程的优点：
# 1.缩短程序的执行时间，提升性能
# 2.改善用户的体验，让用户有更好的体验。


# 调用进程的方法一：

from multiprocessing import Process
# Process 进程
# Thread 线程
import time


def running1():
    while True:
        print('曹宇', end='', flush=True)
        time.sleep(0.01)


def main():
    # Process(target=running1).start()
    p = Process(target=running1)
    p.start()
    while True:
        print('嘿', end='', flush=True)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
#
#
#
# 调用方法二：返回值是零，表示正常结束，False,显示非零。

# import subprocess
#
#
# def main():
#     subprocess.call('calc')
#     subprocess.call('')
#
#
# if __name__ == '__main__':
#     main()


from multiprocessing import Process


count = 0


def running(string):
    global count
    inner = 0
    while count < 100:
        print(string, end='', flush=True)
        count += 1
        inner += 1
    print('%s打印了%s次' % (string, inner))


def main():
    t1 = Process(target=running, args=('🙂',))
    t1.start()
    t2 = Process(target=running, args=('哼',))
    t2.start()


if __name__ == '__main__':
    main()

