"""Diamond"""

def drawing(size):
    """-"""
    count = 0
    while size >= 0:
        space = size // 2
        print(' ' * space, end='')
        if count:
            print('*', end='')
            print(' ' * count, end='')
        print('*')
        size -= 2
        if count == 1:
            count += 1
        count += 1
drawing(int(input()))