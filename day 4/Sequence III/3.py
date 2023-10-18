"""Swquence III"""

def main(jumnuan):
    """_"""
    for row in range(jumnuan):
        for col in range(jumnuan):
            print(col + row + 2, end=" ")
        print()
main(int(input()))
