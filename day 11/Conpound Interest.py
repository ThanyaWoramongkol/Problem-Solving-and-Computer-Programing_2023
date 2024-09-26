"""Compound Interest"""

def torbton(baht, interest, year):
    """-"""
    for _ in range(year):
        baht = baht + baht * (interest/100)
    print('%.2f' % baht)

torbton(int(input()), float(input()), int(input()))
