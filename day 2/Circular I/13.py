"""Circular I"""

def main():
    """_"""
    person_x = float(input())
    person_y = float(input())
    radiant = float(input())
    mosquiter_x = float(input())
    mosquiter_y = float(input())
    distance = (((mosquiter_x - person_x) ** 2) + ((mosquiter_y - person_y) ** 2)) ** 0.5
    if radiant >= distance:
        print("Yes")
    else:
        print("No")

main()
