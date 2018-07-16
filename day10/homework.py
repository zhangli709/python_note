# 上面的时钟，不传参数，直接取系统的时间。
from time import sleep
import time
from text import timerLocal

# class Timer(object):
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def run(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute +=1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def appear(self):
#         return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)
#
#
# def clock():
#
#     time1 = Timer()
#     time1.hour = int(time.strftime('%H', time.localtime()))
#     time1.minute = int(time.strftime('%M', time.localtime()))
#     time1.second = int(time.strftime('%S', time.localtime()))
#     while True:
#         print(time1.appear())
#         sleep(1)
#         time1.run()
#
#
# if __name__ == '__main__':
#     clock()


# 倒计时时钟！ 30分钟倒计时

from time import sleep
from time import time

# class Clock(object):
#
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def run(self):
#         self.second -= 1
#         if self.second == 0:
#             if self.minute > 0:
#                 self.minute -= 1
#                 self.second = 60
#             elif self.minute == 0:
#                 print('时间到!')
#                 return False
#         return True
#
#     def appear(self):
#         print('%02d:%02d:%02d' % (self.hour, self.minute, self.second))
#
# def main():
#     clock = Clock(0, 0, 10)
#     is_go_on = True
#
#     while is_go_on:
#
#         clock.appear()
#         sleep(1)
#         is_go_on = clock.run()
#
#
# if __name__ == '__main__':
#     main()


# 和电脑猜拳


# from random import randint, randrange
#
#
# class Guess_number(object):
#
#     def __init__(self, answer):
#         self.answer = answer
#
#     def compare(self, my_number):
#         if my_number > self.answer:
#             print('小一点！')
#             return True
#         if my_number < self.answer:
#             print('大一点！')
#             return True
#         if my_number == self.answer:
#             print('恭喜你猜对了！')
#             return False
#
#
# def main():
#     answer = randrange(int(input('请输入你要猜的范围：')))
#     is_go_on = True
#     while is_go_on:
#         me = Guess_number(answer)
#         my_number = int(input('请输入你要猜的数：'))
#         is_go_on = me.compare(my_number)
#
#
# if __name__ == '__main__':
#     main()
