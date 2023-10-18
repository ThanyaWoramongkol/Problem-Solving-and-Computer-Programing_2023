"""distribute"""
def paad():
    """midterm 2023"""
    total = int(input())
    people = int(input())
    if total < people:
        print(-1)
    else:
        eight = total // 8
        weise = total % 8
        if weise == 0:
            kon = people - eight
        elif weise != 0:
            kon = people - (eight + 1)
        if total - people < 7:
            print(0)
        elif eight == people and weise == 0:
            print(people)
        elif eight == people and weise != 0:
            print(eight - 1)
        elif eight > people:
            print(people - 1)
        elif eight < people and weise > kon:
            if weise == 4:
                print(eight - 1)
            else:
                print(eight)
        elif eight < people and weise < kon:
            print(eight - 1)
paad()
