class Rect(object):

    def __init__(self, width=0, high=0):
        self._width = width
        self._high = high

    @property
    def width(self):
        return self._width

    @property
    def high(self):
        return self._high

    def perimeter(self):
        print('周长为%02d' % ((self.high + self.width) * 2))

    def area(self):
        print('面积为%02d' % (self.width * self.high))


def main():
    rect = Rect(4, 10)
    rect.perimeter()
    rect.area()

if __name__ == '__main__':
    main()