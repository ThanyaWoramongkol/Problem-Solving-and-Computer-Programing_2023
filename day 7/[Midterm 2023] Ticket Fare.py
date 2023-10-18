"""Ticket Fare"""

def train():
    """-"""
    station, a_station, price1, c_station = int(input()), int(input()), int(input()), int(input())
    price2, price3, start, end = int(input()), int(input()), int(input()), int(input())
    go_to = abs(start - end)
    if go_to <= a_station:
        finish = price1
    elif go_to <= (a_station + c_station):
        finish = price1 + price2 * (go_to - a_station)
    else:
        finish = price1 + price2 * c_station + price3 * (go_to - (a_station + c_station))
    if end > station or start > station:
        finish = "Error"
    print(finish)
train()
