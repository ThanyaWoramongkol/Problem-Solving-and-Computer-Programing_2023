"""pedponfire"""

def fire(ped, abt):
    """ponfire"""
    count = 0
    for i in range(len(ped)): #mark
        for j in range(i + 1, len(ped)):
            if sum([ped[i], ped[j]]) == abt:
                count += 1 #
    print(count)
fire([int(input()) for _ in range(int(input()))], int(input()))

