"""Bonus"""

def money(income, year, month):
    """income * year"""
    if month >= 10:
        year += 1
    if year > 20:
        year = 20
    bonus = income * year
    if bonus < 5000:
        bonus = 5000
    elif bonus > 1000000:
        bonus = 1000000
    return bonus

print(money(int(input()), int(input()), int(input())))
