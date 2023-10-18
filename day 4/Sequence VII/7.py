"""Sequence VII"""

def draw(jumnuan):
    """triangle sleep"""
    for row in range(jumnuan):
        for col in range(jumnuan):
            if row >= col:
                print(col+1, end=' ')
        print()
    for row in range(jumnuan-1, 0, -1):
        for col in range(jumnuan):
            if row > col:
                print(col+1, end=' ')
        print()
draw(int(input()))
