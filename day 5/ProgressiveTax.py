"""ProgressiveTax"""

def first(money):
    """150,001 - 300,000"""
    return (money - 150000) * 0.05

def second(money):
    """300,001 - 500,000"""
    return (money - 300000) * 0.1

def thirth(money):
    """500,001 - 750,000"""
    return (money - 500000) * 0.15

def fourth(money):
    """750,001 - 1,000,000"""
    return (money - 750000) * 0.2

def fifth(money):
    """1,000,001 - 2,000,000"""
    return (money - 1000000) * 0.25

def sixth(money):
    """2,000,001 - 4,000,000"""
    return (money - 2000000) * 0.3

def seventh(money):
    """ > 4,000,001 """
    return (money - 4000000) * 0.35

def tax(income):
    """-"""
    if income > 4000000:
        spend = first(300000) + second(500000) + thirth(750000) \
        + fourth(1000000) + fifth(2000000) + sixth(4000000) + seventh(income)
    elif income > 2000000:
        spend = first(300000) + second(500000) + thirth(750000) \
        + fourth(1000000) + fifth(2000000) + sixth(income)
    elif income > 1000000:
        spend = first(300000) + second(500000) + thirth(750000) \
        + fourth(1000000) + fifth(income)
    elif income > 750000:
        spend = first(300000) + second(500000) + thirth(750000) \
        + fourth(income)
    elif income > 500000:
        spend = first(300000) + second(500000) + thirth(income)
    elif income > 300000:
        spend = first(300000) + second(income)
    elif income > 150000:
        spend = first(income)
    else:
        spend = 0
    print(int(spend))

tax(float(input()))
