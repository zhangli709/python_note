# from random import randrange, randint
#
#
# class Fighter(object):
#
#     def __init__(self, name, hp):
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def hp(self):
#         return self._hp if self._hp >0 else 0
#
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp
#
#     def alive(self):
#         return self._hp > 0
#
#
# class Ultraman(Fighter):
#
#     def __init__(self, name, hp, mp):
#         super(Ultraman, self).__init__(name, hp)
#         self._mp = mp
#
#     @property
#     def mp(self):
#         return self._mp
#
#     @mp.setter
#     def mp(self, mp):
#         self._mp = mp
#
#     def attack(self, m):
#             m.hp -= randrange(15, 25)
#
#     def magic_attack(self, ms):
#         if self._mp >= 20:
#             self._mp -= 20
#             for m in ms:
#                 m.hp -= randrange(10, 15)
#                 return True
#         return False
#
#     def huge_attack(self, m):
#         if self.mp >= 50:
#             self._mp -= 50
#             injury = m.hp * 3 / 4 if m.hp * 3 /4 > 50 else 50
#             m.hp -= injury
#         else:
#             self.attack(m)
#
#     def resume(self):
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name +\
#             '生命值：%d\n' % self._hp +\
#             '魔法值: %d\n' % self._mp
#
# class Monster(Fighter):
#
#     def attack(self, u):
#         u.hp -= randrange(5, 15)
#
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#                '生命值：%d\n' % self.hp
#
# def select_a_monster(monsters):
#     while True:
#         index = randrange(3)
#         monster = monsters[index]
#         if monster.hp > 0:
#             return monster
#
# def is_any_alive(monsters):
#     for monster in monsters:
#         if monster.hp > 0:
#             return True
#
# def display_info(u, ms):
#     print(u)
#     for m in ms:
#         print(m, end='')
#
#
# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('曹宇', 200)
#     m2 = Monster('杨茜然', 300)
#     m3 = Monster('张超', 400)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive() and is_any_alive(ms):
#         print('=============第%d回合===============' % fight_round)
#         m = select_a_monster(ms)
#         skill = randint(1, 10)
#         if skill <= 6:
#
#             u.attack(m)
#             print('%s奥特曼普通攻击了%s小怪兽' %(u.name, m.name))
#             print('%s奥特曼的魔法值恢复了%s' % (u.name, u.resume()))
#         elif skill <= 9:
#             if u.magic_attack(ms):
#                 print()
#         else:
#             if u.huge_attack(m):
#                 print('%s奥特曼使用必杀虐了%s小怪兽' %(u.name, m.name))
#             else:
#                 print('%s奥特曼使用普通攻击击打了%s' %(u.name, m.name))
#                 print('%s奥特曼的魔法值恢复了%s' %(u.name, u.resume()))
#         if m.alive():
#             m.attack(u)
#             print('%s小怪兽回击了%s奥特曼' % (m.name, u.name))
#         display_info(u, ms)
#         fight_round += 1
#         if u.alive():
#             print('%s奥特曼胜利' % u.name)
#         else:
#             print('小怪兽胜利')
#
#
# if __name__ == '__main__':
#     main()


class Account(object):

    def __init__(self, *,card_no, owner, balance):
        self._card_no = card_no
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        if money > 0:
            self._balance += money
            return True
        return False

    def withdraw(self, money):
        if 0 <= money <= self._balance:
            self._balance -= money
            return True
        return False

    def transfer(self, other, money):
        if self.withdraw(money):
            other.deposit(money)

def main():
    account1 = Account(card_no='121525', owner='zl', balance=19999)
    account1.deposit(1)
    print(account1.balance)
    account1.withdraw(10000)
    print(account1.balance)
    account2 = Account(card_no='110', owner='zj', balance=2000)
    account1.transfer(account2, 1000)
    print(account2.balance)


if __name__ == '__main__':
    main()