"""_"""
def main():
    """_"""
    point = 0
    ace = False
    krung = int(input())
    while krung > 0:
        card = input()
        if card == "K" or card == "Q" or card == "J":
            point += 10
        elif card == "A":
            point += 11
            ace = True
        elif card.isdecimal():
            point += int(card)
        krung -= 1
    if ace:
        while point > 21:
            point -= 10
    print(point)
main()
