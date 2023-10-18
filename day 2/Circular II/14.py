"""Circular II"""

def main():
    """_"""
    person_x = float(input())
    person_y = float(input())
    radiant_person = float(input())
    friend_x = float(input())
    friend_y = float(input())
    radiant_friend = float(input())
    distance = (((friend_x - person_x) ** 2) + ((friend_y - person_y) ** 2)) ** 0.5
    if radiant_person + radiant_friend > distance:
        print("Yes")
    else:
        print("No")

main()
