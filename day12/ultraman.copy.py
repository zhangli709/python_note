from random import randrange, randint


class Fighter(object):

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0


class Ultraman(Fighter):

    def __init__(self, name, hp, mp):
        super(Ultraman, self).__init__(name, hp)
        self._mp = mp

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        self._mp = mp

    def attack(self, monster):
            monster.hp -= randrange(15, 25)

    def magic_attack(self, monsters):
        if self._mp >= 20:
            self._mp -= 20
            for monster in monsters:
                monster.hp -= randrange(10, 20)
            return True
        else:
            return False

    def huge_attack(self, monster):
        if self._mp >= 50:
            self._mp -= 50
            injury = monster.hp * 3 // 4
            injury = injury if injury > 50 else 50
            monster.hp -= injury
            return True
        else:
            self.attack(monster)
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
                '生命值：%d\n' % self._hp + \
                '魔法值：%d\n' % self._mp


class Monster(Fighter):

    def attack(self, ultraman):
        ultraman.hp -= randrange(15, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
                '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.hp > 0:
            return True
    else:
        return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')


def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('曹宇', 500)
    m2 = Monster('杨茜然', 500)
    m3 = Monster('张超', 500)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=======第%02d回合=========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法恢复了%d点' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击' % u.name)
            else:
                print('%s使用魔法失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀虐了%s' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive:
            print('%s回击了%s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n=======战斗结束========\n')
    if u.alive:
        print('%s奥特曼胜利！' % u.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()