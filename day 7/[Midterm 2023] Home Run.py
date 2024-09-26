"""home run"""

def mewin(jumnuan, power):
    """-"""
    homie = 0
    for _ in range(jumnuan):
        stage = float(input())
        if power > stage:
            homie += 1
    print(homie)
mewin(int(input()), float(input()))
