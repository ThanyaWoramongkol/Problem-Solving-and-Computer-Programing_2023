"""Meteiorite"""

def ukabard(namnak, raberd, noi):
    """-"""
    count = 0
    med = 1
    while namnak >= noi:
        namnak = namnak / raberd
        count += med
        med = med * raberd
    print(count)
ukabard(float(input()), int(input()), float(input()))
