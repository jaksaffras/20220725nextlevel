from carddeck import CardDeck, Card

class Spam():
    def barf(self):
        print("barf barf barf")

class JokerDeck(CardDeck, Spam):

    def _make_deck(self):
        super()._make_deck()  # call method in superclass
        for _ in range(2):
            joker = Card('Joker', None)
            self._cards.append(joker)


