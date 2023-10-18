"""Sequence V"""

def draw(jumnuan):
    """_"""
    col = 1
    for row in range(jumnuan, 0, -1):
        print(row, end=' ')
        if col == 7:
            print()
            col = 1
        else:
            col += 1
draw(int(input()))
