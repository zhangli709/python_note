"""
类名，每个单词首字母大写
类，属性和行为都要有！
类的定义:
  1.类是对象的蓝图和模板，有了类就可以创建对象
  2.定义类需要做两件事情：数据抽象和行为抽象
  3.数据抽象：抽取对象共同的静态特征（找名词）- 属性
  4，行为抽象：抽取对象共同的动态特征（找动词）- 方法
  定义类的关键字- color-类名（每个单词首字母大写）



class Student(object):  # Python3 中的规范写法

    # 构造方法（构造器/构造子）constructor
    # 调用该方法的时候不是直接使用方法的名字，而是使用类的名字
    def __init__(self, name, age):
        # 给对象绑定属性
        self.name = name
        self.age = age

    # 我们定义一个方法，就代表对象可以接受这个消息。
    # 对象的方法的第一个参数都是统一写成self
    # 他代表了接受消息的对象-对象.消息（参数）
    def study(self, course):  # 行为
        print('%s正在学习%s' % (self.name, course))

    def watch_av(self):  # 行为
        if self.age >= 18:
            print('%s正在观看岛国爱情动作片' % self.name)
        if self.age < 18:
            print('%s，我们推荐你看喜羊羊' % self.name)


def main():
    # step2 调用构造方法创建学生对象
    # 实际上调用的是Student中的__init__方法。
    stu1 = Student('张立', 24)  # 定义一个对象
    # step3 给对象发消息。
    # 通过给对象发消息，让对象完成某些工作，就可以实现程序的功能
    # 解决任何事情，都是通过让对象去做事情。
    stu1.study('Python程序设计')  # 使用行为
    stu2 = Student('曹宇', 1)  # 定义一个对象
    stu2.watch_av()  # 使用行为
    stu2.study('功夫')  # 使用行为


if __name__ == '__main__':
    main()
"""









# 时钟类！

# from rectangle import Timer
# from time import sleep
# from os import system
#
# def main():
#     time = Timer(23, 59, 59)
#     while True:
#         system('cls')
#         print(time.show())
#         sleep(1)
#         time.run()
#
#
# if __name__ == '__main__':
#     main()

#  作业：
# 倒计时时钟！ 30分钟倒计时
# 上面的时钟，不传参数，直接取系统的时间。
# 总结，博客。
# 奥特曼打小怪兽！ hp,mp ,大技能，小技能， 小BOSS
# 描述平面上的一个点，方法：移动这个点，1.移动到某个地方，2.移动多少 3. 移动了多少距离。


from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy
        return self._x, self._y

    def move_to(self, x, y):
        self._x = x
        self._y = y
        return self._x, self._y

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._x - other._y
        return sqrt(dx**2 + dy**2)


def main():
    point = Point()
    P1 = Point(5, 6)
    print(point.move_by(1, 1))
    print(point.move_to(2, 4))
    print(point.distance_to(P1))


if __name__ == '__main__':
    main()