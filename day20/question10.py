"""

题目10: “四川麻将”共有108张牌，分为“筒”、“条”、“万”三种类型，每种类型的牌有1~9的点数，
每个点数有4张牌；游戏通常有4个玩家，游戏开始的时候，有一个玩家会拿到14张牌（首家），
其他三个玩家每人13张牌。要求用面向对象的方式创建麻将牌和玩家并实现洗牌、摸牌以及玩家按照
类型和点数排列手上的牌的操作，最后显示出游戏开始的时候每个玩家手上的牌。

"""
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

        return '%s%s' % (self._suite, self._face)


class Mahjong(object):

	def __init__(self):
		self._cards = []  # 一个引用，没有引用到对象，暂时先占空间
		self._current = 0
		for suite in '万条筒'* 4:
			for face in range(1, 10):
				card = Card(suite, face)
				self._cards.append(card)

	@property
	def cards(self):
		return self._cards

	def shuffle(self):
		"""洗牌"""
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
    return card.suite,card.face








def main():

	def display(players):
		for player in players:
			print(player.name + ':', end=' ')
			player.arrange()
			for card in player.cards_on_hand:
				print(card, end=' ')
			print()
	mahjong = Mahjong()
	players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
	mahjong.shuffle()
	for _ in range(13):
		for player in players:
			player.get(mahjong.next)
	players[0].get(mahjong.next)


	display(players)


if __name__ == '__main__':
	main()
