# 数据的存储 -- 云存储。

## 多重继承 -- 一个类继承多个类 ，而多个父类又有公共的父类（菱形继承/钻石继承）
# 如果一个类有多个父类，那么在搜索属性和方法时，搜索的依据是C3算法
# 这是Python3的改进，在此之前的算法是深度优先搜索算法 DFS

# 避免使用多重继承， 如果必须用，尽量只继承亲爸的，后爸的不继承属性，且继承的方法变为抽象方法。
# 学会分辨继承的到底是那个父类。

from abc import ABCMeta,abstractmethod


class Father(object):

    def __init__(self, name):
        self._name = name

    def drink(self):
        print(self._name + '正在喝二锅头！')


class Monk(object, metaclass=ABCMeta):

    @abstractmethod
    def eat_vegetable(self):
        pass


class Art(object, metaclass=ABCMeta):

    @abstractmethod
    def play_piano(self):
        pass

    @abstractmethod
    def drink(self):
        pass


class Son(Father, Monk, Art):
    """
    多重继承
    """

    def __init__(self, name, nickname, art_name):
        """
        继承了三个父类。
        :param name:
        :param nickname:
        :param art_name:
        """
        Father.__init__(self, name)
        self._nickname = nickname
        self.art_name = art_name

    def drink(self):
        print(self._name + '正在喝鹤顶红')

    def play_piano(self):
        print(self.art_name + '正在谈情')

    def eat_vegetable(self):
        print(self._nickname + '正在吃一日断肠散')


def main():
    son = Son('曹宇', '曹昊天', '曹大师')
    son.drink()
    son.play_piano()
    Father.drink(son)  # 就是想继承后爸的属性的方法！ 默认是继承亲爸的方法。
    son.eat_vegetable()


if __name__ == '__main__':
    main()


## ENIAC 



