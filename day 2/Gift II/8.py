"""gift I"""
def main():
    """_"""
    box = []
    weight_1 = int(input())
    if weight_1 % 2 == 0:
        box.append(weight_1)
    weight_2 = int(input())
    if weight_2 % 2 == 0:
        box.append(weight_2)
    weight_3 = int(input())
    if weight_3 % 2 == 0:
        box.append(weight_3)
    weight_4 = int(input())
    if weight_4 % 2 == 0:
        box.append(weight_4)
    weight_5 = int(input())
    if weight_5 % 2 == 0:
        box.append(weight_5)
    weight_6 = int(input())
    if weight_6 % 2 == 0:
        box.append(weight_6)
    weight_7 = int(input())
    if weight_7 % 2 == 0:
        box.append(weight_7)
    weight_8 = int(input())
    if weight_8 % 2 == 0:
        box.append(weight_8)
    print(*box)
main()
