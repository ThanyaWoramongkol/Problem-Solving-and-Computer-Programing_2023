"""Sequence VIII"""

def draw(jumnuan):
    """triangle flip"""
    for row in range(jumnuan):
        for col in range(row, jumnuan-1):
            print('  ', end=' ')
        for col in range(row+1):
            print('%02d' % (col + 1), end=' ')
        print()
draw(int(input()))
