"""Calculator"""

def calc(jumnuan):
    """-"""
    count = 0
    for i in range(1, jumnuan+1):
        if jumnuan == 1:
            count = 1
            break
        elif len(str(i)) == 1:
            count += 2
            continue
        elif len(str(i)) >= 2 and i != jumnuan:
            count += 1 + len(str(i))
            continue
        else:
            count += 1 + len(str(i))
    return count
print(calc(int(input())))
