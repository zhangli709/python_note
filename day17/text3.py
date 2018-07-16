# from threading import Thread
#
#
# class Patten(Thread):
#
#     def __init__(self, string, count):
#         super(Patten, self).__init__()
#         self._string = string
#         self._count = count
#
#     def run(self):
#         # for _ in range(self._count):
#         #     print(self._string, end='', flush=True)
#         inner = 0
#         while inner < self._count:
#             inner += 1
#             print(self._string, end='', flush=True)
#         return inner
#
#
# def main():
#     p1 = Patten('上', 10000)
#     p1.start()
#     p2 = Patten('右', 10000)
#     p2.start()
#     p3 = Patten('下', 10000)
#     p3.start()
#     p4 = Patten('左', 10000)
#     p4.start()
#     p5 = Patten('中', 10000)
#     p5.start()
#     total = int(p1._count) + int(p2._count) + int(p3._count) + int(p4._count) + int(p5._count)
#     print(total)
#
# if __name__ == '__main__':
#     main()



from multiprocessing import Process


class Patten(Process):

    def __init__(self, string, count):
        self._string = string
        self._count = count
        super(Patten, self).__init__()

    @property
    def count(self):
        return self._count

    def run(self):
        for _ in range(self._count):
            print(self._string, end='', flush=True)


def main():
    patten = Patten('👌', 10000)
    patten2 = Patten('😵', 10000)
    patten3 = Patten('😭', 10000)
    patten4 = Patten('ヾ(•ω•`)o', 10000)
    patten5 = Patten('😀', 10000)
    total = patten.count + patten2.count + patten3.count + patten4.count + patten5.count
    print(total)


if __name__ == '__main__':
    main()

