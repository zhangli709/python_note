from math import gcd


class Fraction(object):

    def __init__(self, num, den):
        if den == 0:
            raise ValueError('分母不能为零')
        self._num = num
        self._den = den
        self.simplify()
        self.normalize()

    def simplify(self):
        i = gcd(self._den, self._num)
        self._num = self._num // i
        self._den = self._den // i

    def normalize(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num

    def __str__(self):
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '%d/%d' % (self._num, self._den)

    def add(self, other):
        return Fraction(self._num * other._den + self._den * other._num, self._den * other._den)

    def sub(self, other):
        return Fraction(self._num * other._den - self._den * other._num, self._den * other._den)

    def mul(self, other):
        return Fraction(self._num * other._num, self._den * other._den)

    def div(self, other):
        return Fraction(self._num * other._den, self._den * other._num)


def main():
    f1 = Fraction(1, 1)
    f2 = Fraction(1, 4)
    print(f1.add(f2))
    print(f1.sub(f2))
    print(f1.mul(f2))
    print(f1.div(f2))


if __name__ == '__main__':
    main()