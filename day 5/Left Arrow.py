"""Right Arrow"""

def drawing(size, height):
    """_"""
    for space in range(height//2 + 1):
        print(" " * space, end='')
        print("*" * size)
    space = height // 2 - 1
    while space >= 0:
        print(" " * space, end="")
        print("*" * size)
        space -= 1
drawing(int(input()), int(input()))
