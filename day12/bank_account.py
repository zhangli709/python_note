# class Bank_account(object):
#
#     def __init__(self, account_number, remaining_sum ):
#         self._account_number = account_number
#         self._remaining_sum = remaining_sum
#         self._money = 0
#
#     @property
#     def account_number(self):
#         return self._account_number
#
#     @property
#     def remaining_sum(self):
#         return self._remaining_sum
#
#     @remaining_sum.setter
#     def remaining_sum(self, remaining_sum):
#         self._remaining_sum = remaining_sum
#
#     @property
#     def money(self):
#         return self._money
#
#     @money.setter
#     def money(self, money):
#         self._money = money
#
#     def inquire(self):
#         print('还剩%s钱' % self._remaining_sum)
#
#     def draw_money(self, money):
#         if money <= self._remaining_sum:
#             self._remaining_sum -= money
#             print('您取出了%s' % money)
#         elif money > self._remaining_sum:
#             print('余额不足！')
#
#     def save_money(self, money):
#         self._remaining_sum += money
#         print('你存入了%s' % money)
#
#     def transfer_account(self, money, other):
#         if money <= self._remaining_sum:
#             self._remaining_sum -= money
#             other._remaining_sum += money
#         if money > self._remaining_sum:
#             print('余额不足')
#
#
# class Zl_account(Bank_account):
#
#     pass
#
#
# class Cy_account(Bank_account):
#     pass
#
#
# def main():
#     me = Zl_account(110, 100000)
#     cy = Cy_account(119, 1000)
#     me.inquire()
#     cy.inquire()
#
#
#
# if __name__ == '__main__':
#     main()

class Account(object):

    def __init__(self, *, card_no, owner, balance=0):
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
        if 0 < money <= self._balance:
            self._balance -= money
            return True
        return False

    def transfer(self, other, money):
        if self.withdraw(money):
            other.deposit(money)
            return True
        return False


def main():
    account = Account(card_no='121525', owner='曹宇', balance=2000)
    print(account.balance)
    account.deposit(2000)
    print(account.balance)
    account.withdraw(1000)
    print(account.balance)
    account2 = Account(card_no='110', owner='张立', balance=100000)
    if account.transfer(account2, 2000):
        print(account.balance)
        print(account2.balance)
    else:
        print('余额不足')

    print(account.balance)


if __name__ == '__main__':
    main()
