"""Tax"""

def first(size):
    """0-600"""
    return size * 0.5

def second(size):
    """601-1800 == 1200"""
    return size * 1.5

def third(size):
    """> 1801 == size - 1800"""
    return size * 4

def pee(year):
    """tax of year"""
    if year >= 10:
        return 0.5
    elif year == 9:
        return 0.6
    elif year == 8:
        return 0.7
    elif year == 7:
        return 0.8
    else:
        return 0.9

def tax(year, motor):
    """-"""
    if motor > 1800:
        spend = (first(600) + second(1200) + third(motor - 1800)) \
        * (1 if year < 6 else pee(year))
    elif motor > 600:
        spend = (first(600) + second(motor - 600)) * \
        (1 if year < 6 else pee(year))
    else:
        spend = first(motor) * (1 if year < 6 else pee(year))
    return spend
print("%.2f" % tax(int(input()), int(input())))
