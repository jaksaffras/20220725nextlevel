import inspect
from pdb import set_trace
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Natasha")  # instantiate an object of type CardDeck
print(d1)

print(f"d1.get_dealer(): {d1.get_dealer()}")

print(f"d1.dealer: {d1.dealer}")

d1.dealer = 'Beatrice'

print(f"d1.dealer: {d1.dealer}")

for name in 'Dave', None, 3.4, 'Marty', 8:
    try:
        d1.dealer = name
    except TypeError as err:
        print(err)
    else:
        print(f"d1.dealer: {d1.dealer}")

print(f"d1.cards: {d1.cards}")
print(f"d1.cards[0]: {d1.cards[0]}")
print(f"repr(d1): {repr(d1)}")

d1.shuffle()

print(f"d1.cards: {d1.cards}")

for _ in range(10):
    card = d1.draw()
    print(f"card: {card}")
print()

print(f"d1.get_ranks(): {d1.get_ranks()}")
print(f"CardDeck.get_ranks(): {CardDeck.get_ranks()}")
print(f"d1: {d1}")
print('-' * 60)

j1 = JokerDeck("Bertie")
print(f"j1: {j1}")
j1.shuffle()
print(f"j1.cards: {j1.cards}")
j1.barf()
print()
print(JokerDeck.mro())

print(f"len(d1): {len(d1)}")
print(f"len(j1): {len(j1)}")

d2 = d1 + j1
print(f"d2: {d2}")
print(f"len(d2): {len(d2)}")
print(f"d2.draw(): {d2.draw()}")

# result = d1 - 10   not implemented

CardDeck.bark('woof')
CardDeck.bark('yip')

print(f"inspect.getmodule(d1): {inspect.getmodule(d1)}")

print(f"dir(d1): {dir(d1)}")

dealer = getattr(d1, 'dealer')
print(f"dealer: {dealer}")

if hasattr(d1, '__len__'):
    print(len(d1))

delattr(CardDeck, 'bark')

print(f"dir(d1): {dir(d1)}")

def doit(self):
    print("this is fun. no, really!")


setattr(CardDeck, 'wombat', doit)

d1.wombat()

print(f"dir(d1): {dir(d1)}")

w = getattr(d1, 'wombat')
w()







