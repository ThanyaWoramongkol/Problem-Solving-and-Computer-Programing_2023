"""WPM"""

def adults(spd):
    """continue"""
    if spd > 25:
        print('Slow/Beginner')
    else:
        print('Very Slow')

def wpm(age, spd):
    """-"""
    if age == "Kids":
        if spd > 40:
            print('Very Fast')
        elif spd > 30:
            print('Fast')
        elif spd > 20:
            print('Average')
        elif spd > 10:
            print('Slow')
        else:
            print('Very Slow')
    elif age == "Adults":
        if spd > 80:
            print('Insane')
        elif spd > 65:
            print('Very Fast')
        elif spd > 45:
            print('Fast/Advanced')
        elif spd > 35:
            print('Intermediate/Average')
        else:
            adults(spd)
wpm(input(), int(input()))
