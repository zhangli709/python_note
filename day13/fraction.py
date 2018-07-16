from math import gcd


class Fraction(object):

    def __init__(self, num=1, den=1):  # 后面跟两个下划线，是共有的，如果后面有一个或没有，才是私有的。
        """
        分子分母
        :param num:分子
        :param den: 分母
        """
        if den == 0:
            raise ValueError('分母不能为零')  # 你敢让他为零，我就死给你看
        self._num = num
        self._den = den
        self.normalize()  # 自动调用正常化
        self.simplify()   # 自动调用化简

    @property
    def num(self):
        return self._num

    # @num.setter
    # def num(self, num):
    #     self._num = num

    @property
    def den(self):
        return self._den

    # @den.setter
    # def den(self, den):
    #     self._den = den

    def add(self, other):
        """加法"""
        return Fraction(self._num * other.den + self._den * other.num,
                        self._den * other.den)

    def __add__(self, other):
        """运算符重载/重写"""
        return self.add(other)

    def sub(self, other):
        """减法"""
        return Fraction(self._num * other.den - self._den * other.num,
                        self._den * other.den)

    def __sub__(self, other):
        return self.sub(other)

    def mul(self, other):
        """乘法"""
        return Fraction(self._num * other.num ,
                        self._den * other.den)

    def __mul__(self, other):
        return self.mul(other)

    def truediv(self, other):
        """除法"""
        return Fraction(self._num * other.den ,
                        self._den * other.num)

    def __truediv__(self, other):
        return self.truediv(other)

    def simplify(self):
        """
        化简
        :return:
        """
        if self._num != 0 and self._den != 1:
            factor = gcd(abs(self._num), abs(self._den))
            if factor > 1:
                self._den //= factor
                self._num //= factor

    def normalize(self):
        """
        正规化
        :return:
        """
        if self._den < 0:
            self._num = -self._num
            self._den = -self._den

    def __str__(self):
        """方法的自动调用"""
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '%d/%d' % (self._num, self._den)


def main():
    f1 = Fraction(-1, -3)
    f2 = Fraction(4, 2)
    f3 = Fraction(0, 4)
    print(f1 + f2)
    print(f2 - f1)
    print(f3 * f1)
    print(f1 / f2)


if __name__ == '__main__':
    main()
