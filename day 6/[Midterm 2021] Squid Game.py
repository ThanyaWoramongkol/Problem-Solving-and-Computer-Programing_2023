"""Squid Game"""

def winner():
    """-"""
    count = 1
    point_a = 0
    point_b = 0
    while count <= 10:
        team_a = int(input())
        point_a += team_a
        count += 1
    while count <= 20:
        team_b = int(input())
        point_b += team_b
        count += 1
    if point_a > point_b:
        print("B")
    elif point_a < point_b:
        print("A")
    else:
        print("AB")
winner()
