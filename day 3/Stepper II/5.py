"""Stepper II"""

def main(start, finish):
    """_"""
    if finish > start:
        for i in range(start, finish + 1, 1):
            print(i)
    else:
        for i in range(start, finish - 1, -1):
            print(i)
main(int(input()), int(input()))
