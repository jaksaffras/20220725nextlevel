#!/usr/bin/env python
#
import shutil
import os

shutil.copy('../DATA/alice.txt', 'betsy.txt') # <1>

print("betsy.txt exists:", os.path.exists('betsy.txt'))

shutil.move('betsy.txt', 'fred.txt') # <2>
print("betsy.txt exists:", os.path.exists('betsy.txt'))
print("fred.txt exists:", os.path.exists('fred.txt'))

new_folder = 'remove_me'

os.mkdir(new_folder) # <3>
shutil.move('fred.txt', new_folder)

shutil.rmtree(new_folder) # <5>

print("{} exists:".format(new_folder), os.path.exists(new_folder))

shutil.make_archive('datafiles', 'xztar', '../DATA')
