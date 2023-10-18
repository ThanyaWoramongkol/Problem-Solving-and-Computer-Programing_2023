"""Kaprekars"""
def salted_1(num1, num2, num3, num4):
    """mak1"""
    if num1 >= num2 >= num3 >= num4:
        makmak = str(num1) + str(num2) + str(num3) + str(num4)
    elif num1 >= num2 >= num4 >= num3:
        makmak = str(num1) + str(num2) + str(num4) + str(num3)
    elif num1 >= num3 >= num2 >= num4:
        makmak = str(num1) + str(num3) + str(num2) + str(num4)
    elif num1 >= num3 >= num4 >= num2:
        makmak = str(num1) + str(num3) + str(num4) + str(num2)
    elif num1 >= num4 >= num3 >= num2:
        makmak = str(num1) + str(num4) + str(num3) + str(num2)
    elif num1 >= num4 >= num2 >= num3:
        makmak = str(num1) + str(num4) + str(num2) + str(num3)###
    else:
        makmak = salted_2(num1, num2, num3, num4)
    return int(makmak)

def salted_2(num1, num2, num3, num4):
    """mak2"""
    if num2 >= num1 >= num3 >= num4:
        makmak = str(num2) + str(num1) + str(num3) + str(num4)
    elif num2 >= num1 >= num4 >= num3:
        makmak = str(num2) + str(num1) + str(num4) + str(num3)
    elif num2 >= num3 >= num1 >= num4:
        makmak = str(num2) + str(num3) + str(num1) + str(num4)
    elif num2 >= num3 >= num4 >= num1:
        makmak = str(num2) + str(num3) + str(num4) + str(num1)
    elif num2 >= num4 >= num3 >= num1:
        makmak = str(num2) + str(num4) + str(num3) + str(num1)
    elif num2 >= num4 >= num1 >= num3:
        makmak = str(num2) + str(num4) + str(num1) + str(num3)
    else:
        makmak = salted_3(num1, num2, num3, num4)
    return makmak

def salted_3(num1, num2, num3, num4):
    """mak3"""
    if num3 >= num1 >= num2 >= num4:
        makmak = str(num3) + str(num1) + str(num2) + str(num4)
    elif num3 >= num1 >= num4 >= num2:
        makmak = str(num3) + str(num1) + str(num4) + str(num2)
    elif num3 >= num2 >= num1 >= num4:
        makmak = str(num3) + str(num2) + str(num1) + str(num4)
    elif num3 >= num2 >= num4 >= num1:
        makmak = str(num3) + str(num2) + str(num4) + str(num1)
    elif num3 >= num4 >= num1 >= num2:
        makmak = str(num3) + str(num4) + str(num1) + str(num2)
    elif num3 >= num4 >= num2 >= num1:
        makmak = str(num3) + str(num4) + str(num2) + str(num1)
    else:
        makmak = salted_4(num1, num2, num3, num4)
    return makmak

def salted_4(num1, num2, num3, num4):
    """mak4"""
    if num4 >= num1 >= num2 >= num3:
        makmak = str(num4) + str(num1) + str(num2) + str(num3)
    elif num4 >= num1 >= num3 >= num2:
        makmak = str(num4) + str(num1) + str(num3) + str(num2)
    elif num4 >= num2 >= num1 >= num3:
        makmak = str(num4) + str(num2) + str(num1) + str(num3)
    elif num4 >= num2 >= num3 >= num1:
        makmak = str(num4) + str(num2) + str(num3) + str(num2)
    elif num4 >= num3 >= num1 >= num2:
        makmak = str(num4) + str(num3) + str(num1) + str(num2)
    else:
        makmak = str(num4) + str(num3) + str(num2) + str(num1)
    return makmak

def sugar_1(num1, num2, num3, num4):
    """nak1"""
    if num1 >= num2 >= num3 >= num4:
        naknak = str(num4) + str(num3) + str(num2) + str(num1)
    elif num1 >= num2 >= num4 >= num3:
        naknak = str(num3) + str(num4) + str(num2) + str(num1)
    elif num1 >= num3 >= num2 >= num4:
        naknak = str(num4) + str(num2) + str(num3) + str(num1)
    elif num1 >= num3 >= num4 >= num2:
        naknak = str(num2) + str(num4) + str(num3) + str(num1)
    elif num1 >= num4 >= num3 >= num2:
        naknak = str(num2) + str(num3) + str(num4) + str(num1)
    elif num1 >= num4 >= num2 >= num3:
        naknak = str(num3) + str(num2) + str(num4) + str(num1)
    else:
        naknak = sugar_2(num1, num2, num3, num4)
    return int(naknak)

def sugar_2(num1, num2, num3, num4):
    """nak2"""
    if num2 >= num1 >= num3 >= num4:
        naknak = str(num4) + str(num3) + str(num1) + str(num2)
    elif num2 >= num1 >= num4 >= num3:
        naknak = str(num3) + str(num4) + str(num1) + str(num2)
    elif num2 >= num3 >= num1 >= num4:
        naknak = str(num4) + str(num1) + str(num3) + str(num2)
    elif num2 >= num3 >= num4 >= num1:
        naknak = str(num1) + str(num4) + str(num3) + str(num2)
    elif num2 >= num4 >= num3 >= num1:
        naknak = str(num1) + str(num3) + str(num4) + str(num2)
    elif num2 >= num4 >= num1 >= num3:
        naknak = str(num3) + str(num1) + str(num4) + str(num2)
    else:
        naknak = sugar_3(num1, num2, num3, num4)
    return naknak

def sugar_3(num1, num2, num3, num4):
    """nak3"""
    if num3 >= num1 >= num2 >= num4:
        naknak = str(num4) + str(num2) + str(num1) + str(num3)
    elif num3 >= num1 >= num4 >= num2:
        naknak = str(num2) + str(num4) + str(num1) + str(num3)
    elif num3 >= num2 >= num1 >= num4:
        naknak = str(num4) + str(num1) + str(num2) + str(num3)
    elif num3 >= num2 >= num4 >= num1:
        naknak = str(num1) + str(num4) + str(num2) + str(num3)
    elif num3 >= num4 >= num1 >= num2:
        naknak = str(num2) + str(num1) + str(num4) + str(num3)
    elif num3 >= num4 >= num2 >= num1:
        naknak = str(num1) + str(num2) + str(num4) + str(num3)
    else:
        naknak = sugar_4(num1, num2, num3, num4)
    return naknak

def sugar_4(num1, num2, num3, num4):
    """nak4"""
    if num4 >= num1 >= num2 >= num3:
        naknak = str(num3) + str(num2) + str(num1) + str(num4)
    elif num4 >= num1 >= num3 >= num2:
        naknak = str(num2) + str(num3) + str(num1) + str(num4)
    elif num4 >= num2 >= num1 >= num3:
        naknak = str(num3) + str(num1) + str(num2) + str(num4)
    elif num4 >= num2 >= num3 >= num1:
        naknak = str(num1) + str(num3) + str(num2) + str(num4)
    elif num4 >= num3 >= num1 >= num2:
        naknak = str(num2) + str(num1) + str(num3) + str(num4)
    else:
        naknak = str(num1) + str(num2) + str(num3) + str(num4)
    return naknak

def main():
    """-"""
    number = int(input())
    jumnuan = 0
    while True:
        count = 1
        if number == 6174:
            break
        number = "%04d" % number
        for i in str(number):
            if count == 1:
                num1 = i
            elif count == 2:
                num2 = i
            elif count == 3:
                num3 = i
            elif count == 4:
                num4 = i
            count += 1
        mak = salted_1(int(num1), int(num2), int(num3), int(num4))
        nak = sugar_1(int(num1), int(num2), int(num3), int(num4))
        number = mak - nak
        jumnuan += 1
    print(jumnuan)
main()
