from random import randrange


class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        """花色，牌面"""
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 14:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = self._face
        return '%s%s' % (self._suite, face_str)


class Poker(object):
    """
    一副牌
    """
    def __init__(self):
        self._cards = []   # 一个引用，没有引用到对象，暂时先占空间
        self._current = 0
        for suite in '♠♥♣♦':
            for face in range(2, 15):
                card = Card(suite, face)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """
        洗牌
        :return:
        """
        self._current = 0
        cards_len = len(self._cards)
        for index, card in enumerate(self._cards):
            pos = randrange(cards_len)
            self._cards[index], self._cards[pos] = self._cards[pos], self._cards[index]

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property  # 一般有返回值的，可以用于包装
    def has_next(self):
        """返回一个布尔值，还有没有牌"""
        return self._current < len(self._cards)


class Player(object):

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self):
        self._cards_on_hand.sort(key=get_key)  # 定义了一个函数来排序


def get_key(card):
    """返回点数排序"""
    return card.face


# def main():
#     p = Poker()
#     p.shuffle()
#     players = [Player('张立'), Player('曹宇'), Player('杨茜然'), Player('张超')]
#     # while p.has_next:
#     for _ in range(3):
#         for player in players:
#             player.get(p.next)
#     for player in players:
#         print(player.name + ':', end=' ')
#         player.arrange()
#         for card in player.cards_on_hand:
#             print(card, end=' ')
#         print()


def main():
    p = Poker()
    p.shuffle()
    p1 = Player('闲家')
    p2 = Player('庄家')
    players = [p1, p2]
    is_go_on = False
    while p.has_next:
        for _ in range(2):
            p1.get(p.next)
            p2.get(p.next)
        for player in players:
            print(player.name + ':', end=' ')
            player.arrange()
            for card in player.cards_on_hand:
                print(card, end=' ')
            print()
        if  p1.cards_on_hand[0]





if __name__ == '__main__':
    main()

