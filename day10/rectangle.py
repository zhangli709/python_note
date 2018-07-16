class Rectangle(object):

    def __init__(self, height, width, color, position):
        self._height = height
        self._width = width
        self._color = color
        self._position = position

    def perimeter(self):
        print('周长为%s' % ((self._height + self._width) * 2))

    def area(self):
        """
        计算面积
        :return: 面积
        """
        print('面积为%s' % (self._height * self._width))


def main():
    recta1 = Rectangle(10, 20, 'blue', 'right')
    recta1.perimeter()
    recta1.area()
    recta2 = Rectangle(15, 10, 'orange', 'middle')
    recta2.perimeter()
    recta2.area()


class Timer(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        走字
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):  # ** def __str__(self): 此方法可以获得对象的字符串表达形式，当我们用print打印对象时，会自动调用该方法。
        """
        显示时间
        :return:
        """
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)  # 换行的方法。


from math import pi

# 我们定义一个类，实际上是把数据和操作数据的函数绑定在一起，
# 形成一个逻辑上的整体，这个整体就叫对象
# 而且将来想要使用这个对象时，直接使用这个类就行了。
class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return pi * self._radius ** 2

    def perimeter(self):
        return pi * self._radius * 2


def main():
    r = float(input('请输入游泳池的半径：'))
    big = Circle(r+3)
    small = Circle(3)
    print('围墙的造价为%.2f元' % (big.perimeter() * 32.5))
    print('过道的造价为%.2f元' % ((big.area()-small.area()) * 32.5))


if __name__ == '__main__':
    main()