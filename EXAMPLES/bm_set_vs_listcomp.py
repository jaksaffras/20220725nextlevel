#!/usr/bin/env python

from timeit import Timer

REPEATS = 1000

setup = '''
list_a = list(range(1, 10000))
list_b = list(range(3, 275)) + list(range(897, 983))
'''

codes = [
    '[a for a in list_a for b in list_b if a == b]',
    'set(list_a) & set(list_b)',
]

for code in codes:
    t = Timer(code, setup)
    print("{:60s}{}".format(code, t.timeit(REPEATS)))
    print('-' * 60)
