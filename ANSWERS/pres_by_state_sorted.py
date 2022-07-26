#!/usr/bin/python

with open("../DATA/presidents.txt") as pres_in:
    count_of = {}

    for rec in pres_in:
        flds = rec.split(":")
        state = flds[6]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

print(count_of, '\n')
print(f"count_of.items(): {count_of.items()}")

def by_count(item):
    return -(item[1]), item[0]   # -count, state-name


for state, count in sorted(count_of.items(), key=by_count):
    print(("%-16s %2d" % (state, count)))
