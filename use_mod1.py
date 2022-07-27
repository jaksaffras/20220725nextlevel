import sys

# from pkg.pkg import module
from john.mathlib import geometry

a1 = geometry.rectangle_area(8, 9)
print(f"a1: {a1}")

raw_diameter = input("What is the diameter? ")
diameter = float(raw_diameter)
a = geometry.circle_area(diameter)
print(f"a: {a}")

# module search algorithm
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (of your Python installation)

for path in sys.path:
    print(path)
