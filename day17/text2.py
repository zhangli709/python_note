# 多线程
# 创建线程的两种方法：
# 1. 直接创建Thread对象，并通过target参数指定线程启动后要执行的任务
# 2. （推荐）继承Thread自定义线程，通过重写run方法来指定线程启动后执行的任务



"""第一种方法："""


# from threading import Thread
#
# count = 0
#
#
# def running(string):
#     global count
#     inner = 0  # 两个线程的inner不是一个东西，各是各个。count是公用的。
#     while count < 100:
#
#         print(string, end='', flush=True)
#         count += 1
#         inner += 1
#     print('%s打印了%s次' % (string, inner))
#
#
# def main():
#     # Thread(target=running).start()
#     # 守护线程，随着主线程的停止而停止。如果主线程未完，守护线程就不会停。args里面传入元组。
#     t1 = Thread(target=running, args=('😕',))  # daemon 守护线程。
#     t1.start()
#     t2 = Thread(target=running, args=('😭',))
#     t2.start()
#
#
# if __name__ == '__main__':
#     main()


"""方法二"""

from threading import Thread

class PrintThread(Thread):

    def __init__(self, string, count):
        super(PrintThread, self).__init__()
        self._string = string
        self._count = count

    def run(self):
        for _ in range(self._count):
            print(self._string, end='', flush=True)

def main():
    printThread1 = PrintThread('Ping', 10000)
    printThread1.start()
    printThread2 = PrintThread('😄', 10000)
    printThread2.start()


if __name__ == '__main__':
    main()



#1.五个线程，各加一万个元素，统计是否共放了五万个元素
#2.pygame  五个方块，用五个线程控制跑，颜色速度不一样，跑向终点。





