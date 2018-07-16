# Python 没有从语言层面支持抽象类的概念
# 我们可以通过abc模块来制造抽象类的效果
# 在定义类的时候，通过指定metaclass=ABCMeta可以将类声明为抽象类
# 抽象类是不能创建对象的，抽象类存在的意义是专门拿来给其它类继承
# abc模块中还有一个包装器 abstractmethon
# 通过这个包装器，可以将方法包装为抽象方法，必须要求子类进行重写。


from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name, age):
        """初始化方法"""
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod  # 变型为抽象类，以下的子类继承这个的时候，必须重写这个方法。
    def get_salary(self):
        """计算月薪"""
        pass


class Manager(Employee):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_salary(self):
        return 15000


class Programer(Employee):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._working_hour = 0

    @property
    def working_hour(self):
        return self._working_hour

    # 非必要属性，通过setter方法给出，必要属性，通过属性给出，不轻易修改
    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return self._working_hour * 150


class Salesman(Employee):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._sales = 0

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 5 / 100


def main():
    emps = [
        Manager('曹宇', 22), Programer('杨茜然', 22),
        Manager('张超', 22), Programer('李西北', 22),
        Salesman('刘家咯', 22)
    ]
    for emp in emps:
        # 识别类型,很重要*******
        if isinstance(emp, Programer):
            emp.working_hour = int(input('请输入%s本月工作时间：' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('请输入%s本月销售额：' % emp.name))
        # 同样是接受get_salary这个消息，但是不用员工表现出了不同行为
        # 因为三个子类都重写了这个方法，所以这个方法会表现出多态行为
        print('%s本月工资为：￥%.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()


