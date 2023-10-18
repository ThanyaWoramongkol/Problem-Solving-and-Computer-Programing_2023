"""BloodDonation"""

def blood(history):
    """[age, weight, count]"""
    can = True
    paper = ''
    if 70 >= int(history[0]) >= 60 or history[0] == '17':
        paper = input()
    if not (70 >= int(history[0]) >= 17) or int(history[1]) < 45 or \
    (history[2] == '0' and int(history[0]) > 55):
        can = False
    if paper == 'False':
        can = False
    if can:
        print('Yes')
    else:
        print('No')
blood([input() for _ in range(3)])
