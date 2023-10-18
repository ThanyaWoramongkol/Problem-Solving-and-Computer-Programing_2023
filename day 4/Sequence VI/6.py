"""Sequence VI"""

def draw(jumnuan):
    """triangle"""
    for row in range(jumnuan):
        for col in range(jumnuan):
            if row >= col:
                print(col+1, end=' ')
        print()
draw(int(input()))
