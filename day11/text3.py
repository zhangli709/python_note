# 一个函数返回多个值，元组，列表，集合，字典，均可以
# 函数的递归调用，自己调自己。
# 内存管理，用--堆，不用--垃圾回收（无人引用，即垃圾 sys.getrefcount查看有几个引用对象）。理论上没有内存泄漏风险的。
# import sys
#
# list1 = [1, 2]
# print(sys.getrefcount(list1))

# 4中容器： list tuple dict set 四个。很重要！！！！装别的东西的容器
# 填坑

# from random import randint
#
# #scores = [[0] * 3] * 5  # 不能这样写
#
# scores = [[0] * 3 for _ in range(5)] # right
# for row in range(5):
#     for col in range(3):
#         scores[row][col] = randint(1,100)
# print(scores)


# 面向对象   最重要的一种思想。

class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name if 2 <= len(name) <= 4 else '无名氏'

    @property  # 属性访问器
    def age(self):
        return self._age

    @age.setter  # 属性修改器
    def age(self, age):
        if 15 <= age <=25:
            self._age = age
        else:
            raise ValueError('无效的年龄')

    # 属性删除器
    @age.deleter
    def age(self):
        del self._age

    def study(self,course):
        print('%s正在学习%s' %(self._name, course))

    def watch_av(self,who):
        if self._age > 18:
            print('%s正在看%s的片' % (self._name, who))
        else:
            print('%s快去看思想品德' % self._name)

def main():
    student = Student('曹宇', 24)
    student.age = 22
    student.study('python')
    student.watch_av('苍老师')

if __name__ == '__main__':
    main()