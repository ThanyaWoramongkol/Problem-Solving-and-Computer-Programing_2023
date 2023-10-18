"""Duplicate I"""

def dupe(num, jumnuan):
    """-"""
    sec1 = {input() for _ in range(num)}
    sec2 = {input() for _ in range(jumnuan)}
    result = sorted(list(sec1 & sec2), reverse=True)
    if len(result) == 0:
        print("Nope")
    else:
        print(*result, sep="\n")
dupe(int(input()), int(input()))
