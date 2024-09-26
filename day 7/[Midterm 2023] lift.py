"""Lift"""

def life(jumnuan, namnak):
    """มีแค่ ลิฟท์ นี่แหละที่เอาผมลง"""
    safe = False
    sammary = 0
    for _ in range(jumnuan):
        age = int(input())
        weight = float(input())

        sammary += weight
        if age >= 12:
            safe = True
    if (safe and sammary <= namnak) or not jumnuan:
        print("Safe")
    else:
        print("Not Safe")
life(int(input()), float(input()))
