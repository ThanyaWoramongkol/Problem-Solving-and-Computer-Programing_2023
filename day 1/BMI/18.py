"""BMI"""

def human(name, weight, height):
    """_"""
    bmi = "%s's  BMI = %.2f" % (name, weight / ((height / 100) ** 2))
    return bmi

def people(name, weight, height):
    """_"""
    bmi = "%s's  BMI = %.2f" % (name, weight / ((height / 100) ** 2))
    return bmi

def person(name, weight, height):
    """_"""
    bmi = "%s's  BMI = %.2f" % (name, weight / ((height / 100) ** 2))
    return bmi

def him(name, weight, height):
    """_"""
    bmi = "%s's  BMI = %.2f" % (name, weight / ((height / 100) ** 2))
    return bmi

def she(name, weight, height):
    """_"""
    bmi = "%s's  BMI = %.2f" % (name, weight / ((height / 100) ** 2))
    return bmi

def main():
    """_"""
    kon1 = human(input(), float(input()), float(input()))
    kon2 = people(input(), float(input()), float(input()))
    kon3 = person(input(), float(input()), float(input()))
    kon4 = him(input(), float(input()), float(input()))
    kon5 = she(input(), float(input()), float(input()))
    print("%s\n%s\n%s\n%s\n%s" % (kon1, kon2, kon3, kon4, kon5))
main()
