"""Triangle I"""

def stick():
    """-"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 >= num2 >= num3:
        ccc = num1
        bbb = num2
        aaa = num3
    elif num1 >= num3 >= num2:
        ccc = num1
        bbb = num3
        aaa = num2
    elif num2 >= num1 >= num3:
        ccc = num2
        bbb = num1
        aaa = num3
    elif num2 >= num3 >= num1:
        ccc = num2
        bbb = num3
        aaa = num1
    elif num3 >= num2 >= num1:
        ccc = num3
        bbb = num2
        aaa = num1
    else:
        ccc = num3
        bbb = num1
        aaa = num2

    tongkarm = ccc ** 2
    pakorb = (aaa ** 2) + (bbb ** 2)
    if -0.01 <= tongkarm - pakorb <= 0.01:
        print("Yes")
    else:
        print("No")
stick()
