"""
Miscellaneous math routines

rectangle_area()
circle_area()

"""

import math

def rectangle_area(length, width):
    """
    Calculate the area of a rectangle

    :param length: length of one side
    :param width:  length of the other side
    :return: area
    """
    return length * width

def circle_area(diameter):
    """
    Calculate the area of a circle.

    :param diameter: Diameter of circle
    :return: area
    """
    radius = diameter / 2
    return math.pi * radius ** 2

if __name__ == '__main__':    #  if running as script
    print("RUNNING geometry.py")
    r = rectangle_area(10, 20)
    c = circle_area(80)
    print(r, c)
