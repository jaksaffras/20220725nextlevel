#!/usr/bin/python
from collections import Counter

with open("../DATA/presidents.txt") as pres_in:
    count_of = {}

    for rec in pres_in:
        # term, last_name, first_name, dob, dod, birthplace, birthstate, took_office, left_office, party = ...
        fields = rec.rstrip().split(":")
        state = fields[6]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

for state, count in sorted(count_of.items()):
    print(f"{state:16s} {count:2d}")


with open('../DATA/presidents.txt') as pres_in:
    states = [pres.split(':')[6] for pres in pres_in]
    counts = Counter(states)
    print(counts)

for state, count in sorted(counts.items()):
    print(f"{state:16s} {count:2d}")

help('sorted')
