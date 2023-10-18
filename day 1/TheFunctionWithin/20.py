"""funtion"""

def funf(num):
    """_"""
    num = 2 * num
    return num

def fung(num):
    """_"""
    num = (3 * num ** 4) - (num ** 3) + (2 * num ** 2) + 10
    return num

def funh(num1, num2, num3):
    """_"""
    number_ans = ((num3 + num1) ** 2) - (num1 * num2) + (num2 ** 2)
    return number_ans

def funi(num1, num2, num3, num4):
    """_"""
    number_ans = ((num1 ** 2) + (num2 ** 2) - (num3 ** 2)) / \
    ((num4 ** 2) - (2 * num1 * num4) + (2 * (num1)))
    return number_ans

def main(num1, num2, num3, num4):
    """_"""
    print(funf(funf(num1)))
    print(fung(funf(num1 - num2)))
    print(funh(funf(num1 + num2), funf(num1 + num3), fung(funf(num4 ** 2))))
    print(funi(funh(funf(num1 + num2), funf(num1 - num3), fung(funf(num4 ** 2))), \
    fung(funf(num1 - num2)), funf(funf(funf(funf(funf(num3))))), num4 ** 8))
main(float(input()), float(input()), float(input()), float(input()))
