import random

class Card:
    def __init__(self, suit, rank, id):
        CARDRANK = [x for x in str('A23456789TJQK')]
        CARDSUIT = ['d','s','c']

        self.rank = rank
        self.suit = suit
        self.id = id
        self.name = f'{CARDRANK[rank-1]}{CARDSUIT[suit]}'

    def __repr__(self):
         return self.name

    def __iter__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, Card):
           return self.id < other.id
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Card):
            return self.rank + other.rank

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        else:
            return False

class Deck:
    def __init__(self):
        self.deck = []
        num = 0
        for suit in range(3):
            for rank in range(1,14):
                card = Card(suit, rank, num)
                self.deck.append(card)
                num += 1

    def __getitem__(self,s):
        return self.deck[s]

    def __iter__(self):
        return self


class Board:
    def __init__(self):
        deck = Deck()
        self.spades = [card for card in deck.deck if card.suit == 1]
        self.clubs = [card for card in deck.deck if card.suit == 2]
        self.diamonds = [card for card in deck.deck if card.suit == 0]
        random.shuffle(self.diamonds)
        self.stock = []


class Player:
    players = []

    def __init__(self, name, type='digital'):
        self.name = name
        self.type = type
        self.hand = None
        self.card = '  '
        self.points = 0
        self.games_won = 0
        __class__.players.append(self)

    def __repr__(self):
        return self.name

p1 = Player('Archie')
p2 = Player('You', type='human')


