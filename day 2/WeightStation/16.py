"""WeightStation"""

def main():
    """_"""
    lst = []
    unbalance_low = False
    unbalance_high = False
    average = float(input())
    namnak_1 = float(input())
    lst.append(namnak_1)
    namnak_2 = float(input())
    lst.append(namnak_2)
    namnak_3 = float(input())
    lst.append(namnak_3)
    namnak_4 = ((average * 4) - (namnak_1 + namnak_2 + namnak_3))
    lst.append(namnak_4)

    for i in lst:
        if i < average / 2:
            unbalance_low = True
            continue
        if i > average * 1.5:
            unbalance_high = True
            continue

    if sum(lst) > 15000:
        print("Overweight")
    elif unbalance_low or unbalance_high:
        print("Unbalance")
    else:
        print("Pass %.2f" % namnak_4)
main()
