# 工资结算系统 1. 部门经理 1.5万元/月  2. 程序员 工作时间  150元/小时  3.销售员 1200底薪，+ %5销售额的提成
# 给你员工，得出工资。  员工类，父类  下面3类子类。


class Staff(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Department_manager(Staff):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def get_money(self):
        print('%s岁的%s工作了一个月挣了%s' % (self._age, self._name, self._salary))


class Programer(Staff):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def get_money(self, time):
        print('%s岁的%s工作了一个月共%s小时挣了%s' % (self._age, self._name, time, self._salary * time))


class Salesman(Staff):

    def __init__(self, name, age, sale):
        super().__init__(name, age)
        self._sale = sale

    @property
    def salary(self):
        return self._sale

    def get_money(self):
        salary = self._sale * 5 / 100 + 1200
        print('销售员%s一个月挣了%s' % (self._name, salary))


def main():
    which = str(input('请输入员工类型：部门经理/程序员/销售员'))
    if which == '部门经理':
        name = input('请输入名字')
        age = input('请输入年龄')
        man1 = Department_manager(name, age, '1.5万元')
        print(man1.get_money())
    elif which == '程序员':
        name = input('请输入名字')
        age = input('请输入年龄')
        man2 = Programer(name, age, 150)
        time = int(input('请输入工作了多少小时'))
        print(man2.get_money(time))
    elif which == '销售员':
        name = input('请输入名字')
        age = input('请输入年龄')
        sale = int(input('请输入销售额'))
        man3 = Salesman(name, age, sale)
        print(man3.get_money())


if __name__ == '__main__':
    main()
