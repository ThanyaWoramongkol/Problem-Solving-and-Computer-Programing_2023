"""Parity"""

def binary(bina, evod):
    """-"""
    result = 0
    for i in bina:
        result += int(i)
    if evod == "Even" and result % 2:
        return str(bina) + "1"
    elif evod == "Even" and result % 2 == 0:
        return str(bina) + "0"
    elif evod == "Odd" and result % 2:
        return str(bina) + "0"
    else:
        return str(bina) + "1"
print(binary(input(), input()))
