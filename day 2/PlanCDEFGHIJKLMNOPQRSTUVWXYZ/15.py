"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""

def ascend():
    """_"""
    number_1 = float(input())
    number_2 = float(input())
    number_3 = float(input())
    if number_1 >= number_2 and number_2 >= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_3, number_2, number_1))
        return text
    elif number_1 >= number_2 and number_2 <= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_2, number_3, number_1))
        return text
    elif number_1 <= number_2 and number_2 >= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_3, number_1, number_2))
        return text
    elif number_1 <= number_2 and number_2 >= number_3 and number_1 <= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_1, number_3, number_2))
        return text
    elif number_1 <= number_2 and number_2 <= number_3 and number_1 <= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_1, number_2, number_3))
        return text
    else:
        text = ("%.2f, %.2f, %.2f" % (number_2, number_1, number_3))
        return text

def descend():
    """_"""
    number_1 = float(input())
    number_2 = float(input())
    number_3 = float(input())
    if number_1 >= number_2 and number_2 >= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_1, number_2, number_3))
        return text
    elif number_1 >= number_2 and number_2 <= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_1, number_3, number_2))
        return text
    elif number_1 <= number_2 and number_2 >= number_3 and number_1 >= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_2, number_1, number_3))
        return text
    elif number_1 <= number_2 and number_2 >= number_3 and number_1 <= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_2, number_3, number_1))
        return text
    elif number_1 <= number_2 and number_2 <= number_3 and number_1 <= number_3:
        text = ("%.2f, %.2f, %.2f" % (number_3, number_2, number_1))
        return text
    else:
        text = ("%.2f, %.2f, %.2f" % (number_3, number_1, number_2))
        return text

def main():
    """_"""
    option = input().capitalize()
    if option == "Ascend":
        print(ascend())
    elif option == "Descend":
        print(descend())

main()
