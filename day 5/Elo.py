"""Elo"""

def calc(var_ra, var_rb, function):
    """_"""
    if function == "A":
        result = 1 / (1 + ((10) ** ((var_rb - var_ra) / 400)))
    else:
        result = 1 / (1 + ((10) ** ((var_ra - var_rb) / 400)))
    print("%.2f" % result)

calc(int(input()), int(input()), input())
