from random import randint


class Ultraman(object):

    __slots__ = ('_name', '_hp', '_mp')   # 限定属性数量，只允许有这几个属性

    def __init__(self, name, hp, mp):
        self._name = name
        self._hp = hp
        self._mp = mp

    @property
    def name(self):
        return self._name  # 修饰，

    @property
    def hp(self):  # 修饰
        return self._hp

    @hp.setter  # 修改器
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, monster):
        """
        攻击怪兽，怪兽掉血。
        :param monster:
        :return:
        """
        monster.hp -= randint(15, 25)


    def huge_attack(self, monster):
        """
        如果蓝量大于50，就放大技能：怪兽掉四分之三的血，如果不够扣，直接扣50点血，
        如果蓝量不够，执行普通攻击
        :param monster:
        :return:
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = monster.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            monster.hp -= injury
        else:
            self.attack(monster)

    def magic_attack(self, m1, m2, m3):
        if self._mp >= 20:
            self._mp -= 20
            for i in ms:
                i -= randint(10, 15)

    def __str__(self):
        return '%s奥特曼\n' % self._name + \
                '生命值：%d\n' % self._hp + \
                '魔法值：%d\n' % self._mp


class Monster(object):

    __slots__ = ('_name', '_hp')   # 限制了你的成员变量

    def __init__(self, name, hp):  # 成员变量
        self._name = name
        self._hp = hp

    @property
    def name(self):  # 属性，被包装好的。
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, ultraman):
        ultraman.hp -= randint(10, 20)

    def __str__(self):
        return '%s小怪兽\n' % self._name + \
                '生命值：%d\n' % self._hp


def main():
    u = Ultraman('骆昊', 1000, 120)
    u_is_alive = True
    print(u)
    ms = [Monster('曹宇', 50), Monster('杨茜然', 200), Monster('张超', 150)]
    m1 = ms[0]
    m1_is_alive = True
    m2 = ms[1]
    m2_is_alive = True
    m3 = ms[2]
    m3_is_alive = True
    print(m1, m2, m3)
    fight_round = 1

    while u.hp > 0 :
        # print('===第%d回合===' % fight_round)
        # fight_round += 1
        # u.attack(m)
        # if m.hp > 0:
        #     m.attack(u)
        # print(u)
        # print(m) # 每一个
        i = randint(1, 10)
        print('===第%d回合===' % fight_round)
        fight_round += 1
        if i <= 6:
            if m1_is_alive:
                u.attack(m1)
                if m1.hp > 0:
                    m1.attack(u)
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m1_is_alive = False
                    m2.attack(u)
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m2_is_alive:
                u.attack(m2)
                if m2.hp > 0:
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m2_is_alive = False
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m3_is_alive:
                u.attack(m3)
                if m3.hp > 0:
                    m3.attack(u)
                else:
                    m3_is_alive = False
                print(u)
                print(m1, m2, m3)
        if i <= 9:
            if m1_is_alive:
                u.magic_attack(m1)
                if m1.hp > 0:
                    m1.attack(u)
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m1_is_alive = False
                    m2.attack(u)
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m2_is_alive:
                u.magic_attack(m2)
                if m2.hp > 0:
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m2_is_alive = False
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m3_is_alive:
                u.magic_attack(m3)
                if m3.hp > 0:
                    m3.attack(u)
                else:
                    m3_is_alive = False
                print(u)
                print(m1, m2, m3)
        if i == 10:
            if m1_is_alive:
                u.huge_attack(ms)
                if m1.hp > 0:
                    m1.attack(u)
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m1_is_alive = False
                    m2.attack(u)
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m2_is_alive:
                u.huge_attack(ms)
                if m2.hp > 0:
                    m2.attack(u)
                    m3.attack(u)
                else:
                    m2_is_alive = False
                    m3.attack(u)
                print(u)
                print(m1, m2, m3)
            elif m3_is_alive:
                u.huge_attack(ms)
                if m3.hp > 0:
                    m3.attack(u)
                else:
                    m3_is_alive = False
                print(u)
                print(m1, m2, m3)

        if u.hp > 0:
            print('%s奥特曼胜利' % u.name)
        if m3.hp > 0:
            print('%s小怪兽胜利' % m1.name)

if __name__ == '__main__':
    main()

