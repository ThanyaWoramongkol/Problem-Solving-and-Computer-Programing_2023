"""Harshad Number"""

def harshard():
    """input  10 times if % result = 0 -> Yes"""
    for _ in range(10):
        number = abs(int(input()))
        lst = []
        for i in str(number):
            lst.append(int(i))
        divisor = sum(lst)
        if int(number) == 0:
            print('No')
        elif int(number) % divisor == 0:
            print('Yes')
        else:
            print('No')
harshard()
