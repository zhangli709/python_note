 # 自己创建一个类，来描述数学上的分数，要求有加减乘除的运算，化简，等等
 # 运算符重载。


# class Math(object):
#
#     def __init__(self, add, subtract, multiple, division):
#         self._add = add
#         self._subtract = subtract
#         self.multiple = multiple
#         self.division = division
#
#     @property
#     def add(self):
#         return self._add
#
#     @property
#     def subtract(self):
#         return self._subtract
#
#     @property
#     def multiple(self):
#         return self._multiple
#
#     @property
#     def division(self):
#         return self._division
#
#     def operation(self):


class Grade(object):

    def __init__(self, numerator=1, denominator=1):
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def add(self, other):
        together_denominator = self._denominator * other._denominator
        return (self._numerator * other._denominator + other._numerator * self._denominator) / together_denominator

    def substrct(self, other):
        together_denominator = self._denominator * other._denominator
        return (self._numerator * other._denominator - other._numerator * self._denominator) / together_denominator

    def multiple(self, other):
        return (self._numerator * other._numerator ) / (self._denominator * other._denominator)

    def division(self, other):
        return (self._numerator * other._denominator ) / (self._denominator * other._numerator)


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(2, x + 1):
        if x % i == 0 and y % i == 0:
            return i


def main():
    grade1 = Grade(2, 4)
    grade2 = Grade(3, 5)
    print(grade1.add(grade2))
    print(grade1.substrct(grade2))
    print(grade1.multiple(grade2))
    print(grade1.division(grade2))


if __name__ == '__main__':
    main()
