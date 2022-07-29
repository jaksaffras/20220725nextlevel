#!/usr/bin/env python

from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files, '\n')

no_files = glob('../DATA/*.db')
print(no_files, '\n')

