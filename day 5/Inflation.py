"""Inflation"""

def foe(cost, year):
    """_"""
    money = int(cost) * ((1.0381) ** year)
    output = int(money * 100) / 100
    print(output)
foe(float(input()), int(input()))
