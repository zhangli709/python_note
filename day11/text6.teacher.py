class Teacher(object):

    def __init__(self, name, age, title):
        self._name = name
        self._age = age
        self._title = title

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s正在教%s' % (self._name, course))

    def watch_av(self, who):
        print('%s正在看%s的片' % (self._name, who))


def main():
    teacher = Teacher('骆昊', 38, 'Python')
    print(teacher.name)
    teacher.teach('Python')
    teacher.watch_av('XX老师')


if __name__ == '__main__':
    main()