"""Sequence X"""

def draw(jumnuan):
    """triangle flip"""
    for row in range(jumnuan):
        for col in range(row, jumnuan-1):
            print('  ', end=' ')
        for col in range(row+1):
            print('%02d' % (col + 1), end=' ')
        for col in range(row): #from i to 0
            print('%02d' % (row-col), end=' ')
        print()
    for row in range(jumnuan-1, 0, -1):
        for col in range(row, jumnuan):
            print('  ', end=' ')
        for col in range(row-1):
            print('%02d' % (col+1), end=' ')
        for col in range(row):
            print('%02d' % (row-col), end=' ')
        print()
draw(int(input()))
