import random
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Jack', 'Queen', 'King']


class Card:

    def __init__(self, value):
        if 0 <= value <= 51:
            self.value = value
            self.suit = suits[int(value) // 13]
            self.face = faces[int(value) % 13]
            self.name = '{} of {}'.format(self.face, self.suit)
        else:
            self.value = 52
            self.suit = 'Joker'
            self.face = 'Joker'
            self.name = 'Joker'


class Deck:

    def __init__(self):
        self.contents = [Card(x) for x in range(52)]

    def draw(self):
        if len(self.contents) > 0:
            print(self.contents[-1].name)
            return self.contents.pop()
        else:
            print('Deck is empty')

    def shuffle(self):
        shuffled = []
        for i in range(len(self.contents)):
            rand = random.randrange(len(self.contents))
            shuffled.append(self.contents[rand])
            del self.contents[rand]
        self.contents = shuffled
