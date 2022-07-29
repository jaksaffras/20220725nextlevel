import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.Info)

class Card:
    def __init__(self, rank, suit):
        logger.info("Created deck")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):  # eyeball-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name} {self.rank}-{self.suit}"

    def __repr__(self):  # interpreter-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.rank}', '{self.suit}')"


class CardDeck:
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.CLUB, self.DIAMOND, self.HEART, self.SPADE:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    # @property
    # def cards(self):
    #     return self._cards

    def cards(self):
        return self._cards

    cards = property(cards)

    # getter method (AKA accessor)
    def get_dealer(self):
        return self._dealer

#  self:Python::this:Java

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            wrong_type = type(dealer).__name__
            raise TypeError(f"Dealer must be a string, not '{wrong_type}'")

    @property
    def spam(self):
        return self._spam

    @property
    def ham(self):
        return self._ham

    @ham.setter
    def ham(self, value):
        self._ham = value

    def __str__(self):
        my_name = type(self).__name__
        return f"{my_name}: {self.dealer}"

    def __repr__(self):
        my_name = type(self).__name__
        return f"{my_name}('{self.dealer}')"

    def __len__(self):
        return len(self._cards)

    def __add__(self, other):
        my_class = type(self)
        tmp = my_class(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp


    def shuffle(self):  # instance method
        random.shuffle(self._cards)

    def draw(wombat):
        return wombat._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def bark(kind):
        print(f"{kind} {kind}")
