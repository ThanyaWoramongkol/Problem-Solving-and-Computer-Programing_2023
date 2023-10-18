"""Align"""

def main(size, position, text):
    """_"""
    space = ' ' * ((size - len(text) + 1) // 2)
    if position == "left":
        print(text)
    elif position == "center":
        print(space + text)
    elif position == "right":
        print(" " * (size - len(text)) + text)

main(int(input()), input(), input())
