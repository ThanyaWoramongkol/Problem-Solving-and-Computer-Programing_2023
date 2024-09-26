"""PickThemAgain"""

def pick(numbers):
    """-"""
    number = []
    for i in numbers:
        if not int(i) % 3 or not int(i) % 5 or not int(i):
            number.append(i)
    if number == []:
        print("Nope")
    else:
        print(*number[::-1], sep="\n")

pick(input().split())
