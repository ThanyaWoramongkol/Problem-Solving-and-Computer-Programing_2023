"""Century"""
from math import ceil

def years(count):
    """B.E. 2563 = A.D. 2020"""
    for _ in range(count):
        year = input()
        phe = int(year[5:])
        if "B" in year:
            phe -= 543
        satawat = ceil(phe/100)
        if satawat <= 0:
            print("ERROR")
        else:
            print(satawat)
years(int(input()))
