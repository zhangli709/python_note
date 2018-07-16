import time
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        """当多个线程同时访问一个资源的时候，就有可能因为竞争资源导致状态崩溃
        被多个线程访问的资源，称为临界资源，对临界资源的访问需要加上保护。
        """
        if money:
            self._lock.acquire()  # 加锁，开始是并行，加锁后变成串行，解锁后变成并行。
            try:
                new_balance = self._balance + money
                time.sleep(0.01)
                self._balance = new_balance
            finally:
                self._lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account):
        super(AddMoneyThread, self).__init__()
        self._account = account

    def run(self):
        self._account.deposit(1)


def main():
    account = Account()
    tlist = []
    for _ in range(100):
        t = AddMoneyThread(account)
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()
    print('%d元' % account.balance)


if __name__ == '__main__':
    main()