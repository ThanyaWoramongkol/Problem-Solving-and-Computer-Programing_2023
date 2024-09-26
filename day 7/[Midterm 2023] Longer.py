"""Longer"""
from math import pi

def more(radiant, kwarn, yarw):
    """-"""
    circle = 2 * pi * radiant
    rectangle = kwarn * 2 + yarw * 2
    if circle > rectangle:
        print("Circle is longer\n%.5f" % (circle - rectangle))
    elif rectangle > circle:
        print("Rectangle is longer\n%.5f" % (rectangle - circle))
    else:
        print("Equal\n%.5f" % circle)

more(float(input()), float(input()), float(input()))
