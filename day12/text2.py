from abc import abstractmethod, ABCMeta


class Stuff(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Stuff):

    def get_salary(self):
        return 15000


class Programmer(Stuff):

    def __init__(self, name):
        super(Programmer, self).__init__(name)
        self._working_hour = 0

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 150 * self._working_hour


class Salesman(Stuff):

    def __init__(self, name):
        super(Salesman, self).__init__(name)
        self._sales = 0

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1200 + self._sales * 0.05


def main():
    emps = [
        Programmer('曹宇',), Programmer('杨茜然'), Manager('张立'), Manager('张超'), Salesman('李西北')
    ]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s工作时间：' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('请输入%s销售额：' % emp.name))
        print('%s一个月赚了%s元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
