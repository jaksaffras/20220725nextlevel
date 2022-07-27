from datetime import datetime
from functools import wraps
import logging

logging.basicConfig(filename='deco.log', level=logging.INFO)

# @property
# @staticmethod
# @classmethod

"""
@spam
def ham():
    pass

**same as**

ham = spam(ham)

----------------------------------------
@foo(blah)
def bar():
    pass

** same as **

callable = foo(blah)
bar = callable(bar)

"""


# callback
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f = sorted(fruits, key=str.lower)
print(f"f: {f}")

def toast():
    print("I am TOAST")


def ham(func):
    return toast

@ham
def bark():
    print("Woof woof")

@ham
def meow():
    print("Meoooowwwwww")

def doit(func):
    func()

doit(bark)
doit(meow)

@ham
def spam():
    print("I am SPAM")
# spam = ham(spam)

spam()

bark()
meow()
print()

def timestamp(old_func):

    @wraps(old_func)
    def _replacement(*args, **kwargs):
        logging.info(f"Calling {old_func.__name__} at {datetime.now()}")
        result = old_func(*args, **kwargs)
        return result

    return _replacement

@timestamp
def alpha():
    print("ALPHA!")

@timestamp
def beta():
    print("BETA!")

alpha()
beta()

print(f"alpha.__name__: {alpha.__name__}")
print(f"beta.__name__: {beta.__name__}")

@timestamp
def blub():
    pass

blub()
blub()
blub()

