"""Lotto"""

def lottery():
    """-"""
    prize = 0
    near = []
    #input
    first_prize = input()
    last_two = input()
    first_thirt_1 = input()
    first_thirt_2 = input()
    last_thirt_1 = input()
    last_thirt_2 = input()
    buy = input()
    #near position
    for i in range(1, -2, -2):
        if first_prize == '999999':
            near.append('000000')#+1
            near.append('999998')#-1
            break
        elif first_prize == '000000':
            near.append('000001')#+1
            near.append('999999')#-1
            break
        near_num = "%06d" % (int(first_prize) + i)
        near.append(str(near_num))
    #yeahyeah
    if buy == first_prize:
        prize += 6000000
    if buy[-2:] == last_two:
        prize += 2000
    if buy[0:3] == first_thirt_1:
        prize += 4000
    if buy[0:3] == first_thirt_2:
        prize += 4000
    if buy[-3:] == last_thirt_1:
        prize += 4000
    if buy[-3:] == last_thirt_2:
        prize += 4000
    if buy == near[0] or buy == near[1]:
        prize += 100000

    print(prize)

lottery()
