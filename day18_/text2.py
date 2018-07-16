import time
from threading import Thread


class Account(object):

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        if money > 0:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance


class AddMoneyThread(Thread):

    def __init__(self, account):
        super(AddMoneyThread, self).__init__()
        self._accout = account

    @property
    def account(self):
        return self._accout

    def run(self):
        self._accout.deposit(1)


def main():
    account = Account(0)
    for _ in range(100):
        t = AddMoneyThread(account)
        t.start()
        t.join()
    print(account.balance)


if __name__ == '__main__':
    main()