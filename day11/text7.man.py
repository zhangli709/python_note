# 继承  - 从已经有的类创建新类的过程
# 提供继承信息的称为父类（超类/基类）
# 得到继承信息的称为子类（派生类/衍生类）
# 通过继承我们可以将子类中的重复代码，抽取到父类中。
# 子类通过继承，并复用这些代码，来减少重复代码的编写
# 将来如果要维护子类的公共代码，只需要在父类中进行操作即可


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter 访问器
    @property
    def name(self):
        return self._name

    # setter  修改器
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_av(self, who):
        if self._age > 18:
            print('%s正在看%s的片' % (self._name, who))
        else:
            print('%s只能看喜羊羊' % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 初始化方法！ 调用爸爸的属性，完成属性的绑定。
        self._grade = grade

    def study(self, course):
        print('%s正在学习%s' % (self._name, course))

    # 方法重写 override - 覆盖/置换/覆写
    # 子类继承父类方法之后，对方发进行了重新实现
    # 当我们给子类发送消息时，执行的时子类重写的方法
    def watch_av(self):
        print('学生正在学习技术' )


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s正在教%s' % (self._name, course))

def main():
    teacher = Teacher('骆昊', 38, 'Python')
    student = Student('张立', 24, 66)
    print(teacher.name)
    teacher.teach('Python')
    teacher.watch_av('XX老师')
    print(student.watch_av())


if __name__ == '__main__':
    main()



# 工资结算系统 1. 部门经理 1.5万元/月  2. 程序员 工作时间  150元/小时  3.销售员 1200底薪，+ %5销售额的提成
# 给你员工，得出工资。  员工类，父类  下面3类子类。
