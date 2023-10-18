"""Sequence IV"""

def main(jumnuan):
    """_"""
    for row in range(jumnuan):
        for col in range(jumnuan):
            print(row*jumnuan + col +1, end=" ")
        print()
main(int(input()))
