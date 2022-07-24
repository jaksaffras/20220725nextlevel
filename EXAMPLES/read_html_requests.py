#!/usr/bin/env python

for header, value in sorted(response.headers.items()): # <2>
    print("{:20.20s} {}".format(header, value))
print()

print(response.text[:200])   # <3>
print('...')
print(response.text[-200:])   # <4>
