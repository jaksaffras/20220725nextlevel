#!/usr/bin/env python

import re

FILE_PATH = "../DATA/mary.txt"

# NOTE: r'\W+' is a regular expression that splits on anything that isn't a letter, number, or underscore

with open(FILE_PATH) as mary_in:
    file_contents = mary_in.read()
    s = {w.lower() for w in re.split(r'\W+', file_contents) if w} #<1>
print(s)
