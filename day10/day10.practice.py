# 奥特曼打小怪兽
from random import randrange,randint
from time import sleep


class Super_man(object):

    def __init__(self, hp1=100, mp1=100):
        self._hp1 = hp1
        self._mp1 = mp1

    def attack_it(self, other):
        other.hp -= randint(15, 25)
        if other.hp2 > 0:
            print('奥特曼对怪兽造成了%d点伤害！' % self._attack1)
            return True
        if other._hp2 <= 0:
            print('奥特曼杀死了1只小怪兽！')

            return False



class Monster(object):

    def __init__(self, hp2=10, attack2=2):
        self._hp2 = hp2
        self._attack2 = attack2


    def attack_it(self, other):
        other._hp1 -= self._attack2
        if other._hp1 > 0:
            print('怪兽对奥特曼造成了%d点伤害！' % self._attack2)
            return True
        if other._hp1 <= 0:
            print('奥特曼被杀死了！')
            return False


def main():
    super_man = Super_man(100, 100, 5)

    monster = Monster(10, 2)
    is_go_on = True
    n = randrange(1, 10)
    print('开始有%d只怪兽' % n)

    while is_go_on:
        monster = Monster(10 * n, 2)
        for _ in range(n):
            is_go_on = monster.attack_it(super_man)
            sleep(1)
        if is_go_on == True:
            is_go_on = super_man.attack_it(monster)
        sleep(1)


if __name__ == '__main__':
    main()