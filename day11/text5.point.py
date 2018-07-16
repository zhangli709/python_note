from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x - other.x
        dy = self._y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


class Line(object):

    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property
    def length(self):
        return self._start.distance_to(self._end)


# 线段上有两个点 - has-a --关联 ， 泥中有我，我属于你
# 奥特曼打了小怪兽 - use-a - 依赖，作用和反作用
# 学生是人 - is-a - 继承
def main():
    p1 = Point(3, 5)
    p2 = Point()
    line = Line(p1, p2)
    print(p1)
    print(p2)
    print(line.length)

if __name__ == '__main__':
    main()

