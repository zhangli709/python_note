from random import randint


class Card(object):

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        elif self._face == 14:
            face_str = 'A'
        else:
            face_str = self._face
        return '%s%s' %(self._suite, face_str)

class poker(object):

    def __init__(self):
        self._cards = []
        self._current = 0
        for suite in '♥♠♦♣':
            for face in range(2, 15):
                card = Card(suite, face)
                cards.append(card)
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        for index, val in enumerate(self._cards):
            num = randint(len(self._cards))
            self._cards[index], self._cards[num] = self._cards[num], self._cards[index]

    def next(self):


