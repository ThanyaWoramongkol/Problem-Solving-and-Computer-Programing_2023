"""3nPlus1"""

def plus():
    """-"""
    while True:
        count = 0
        number = int(input())
        if number == 0:
            break
        while True:
            count += 1
            if number == 1:
                break
            if number % 2 == 0:
                number = number / 2
            else:
                number = number * 3 + 1
        print(count)
plus()
