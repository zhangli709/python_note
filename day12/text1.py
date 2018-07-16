from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法， 用以发给类，不是发给对象的。就是发给它爸爸的。
    # @staticmethod   # @classmethod  也是发给类的，区别，
    # def is_valid(a, b, c):
    #     return a + b > c and a + c > b and b + c > a

    @classmethod  # @classmethod  也是发给类的，区别，
    def is_valid(cls, a, b, c):
        return a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self):
        return self._a + self._b + self._c

    @property
    def area(self):
        half = self.perimeter / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a = b = c = 1
    if Triangle.is_valid(a, b, c):  # 静态方法。
        t = Triangle(a, b, c)
        print(t.perimeter)  # 对象来执行
        # 或者用 (Triangle.perimeter(t))  类来执行，传入参数。
        print(t.area)
    else:
        print('无法构成三角形！')


if __name__ == '__main__':
    main()


