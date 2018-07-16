# 分钟倒计时时钟
from time import sleep

class Timer(object):

    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second -= 1
        if self._second == 0:
            if self._minute > 0:
                self._second = 60
                self._minute -= 1
                if self._minute == 0:
                    return False
        return True




    def appear(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    time = Timer(0, 30, 1)
    is_go_on = True
    while is_go_on:
        time.appear()
        sleep(1)
        is_go_on = time.run()




if __name__ == '__main__':
    main()