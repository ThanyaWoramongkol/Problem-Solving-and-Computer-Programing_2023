"""SMS"""

def sms():
    """dictionari"""
    dicnari = {2:('A', 'B', 'C'), 3:('D', 'E', 'F'), 4:('G', 'H', 'I'), \
    5:('J', 'K', 'L'), 6:('M', 'N', 'O'), 7:('P', 'Q', 'R', 'S'), \
    8:('T', 'U', 'V'), 9:('W', 'X', 'Y', 'S')}
    text = []
    time = int(input())
    for _ in range(time):
        button = int(input())
        press = int(input())
        if button > 1:
            text.append(dicnari[button][(press-1) % len(dicnari[button])])
        else:
            remove = min(len(text), press)
            del text[-remove:]
    print(''.join(text) if len(text) > 0 else 'null')
sms()
