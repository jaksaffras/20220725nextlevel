#!/usr/bin/env python
from timeit import Timer

setup_code = """
values = []
"""  # <1>

test_code_one = '''
for i in range(10000):
    values.append(i)
values.clear()
'''  # <2>

test_code_two = '''
i = 0
while i < 10000:
    values.append(i)
    i += 1
values.clear()
'''  # <2>

t1 = Timer(test_code_one, setup_code)  # <3>
t2 = Timer(test_code_two, setup_code)  # <3>

print("test one:")
print(t1.timeit(1000))  # <4>
print()

print("test two:")
print(t2.timeit(1000))  # <4>
print()
