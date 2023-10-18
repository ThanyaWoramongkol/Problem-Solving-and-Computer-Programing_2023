"""Day2011"""

def dayly(day, month):
    """-"""
    monday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    name = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
    daymon = monday[:month-1]
    jumnuan = (sum(daymon) + day) % 7
    print(name[jumnuan])

dayly(int(input()), int(input()))
