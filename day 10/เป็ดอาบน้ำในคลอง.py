"""pedkrapkrap"""

def ped(jumnuan, abt):
    """_"""
    index = 0
    count = 0
    print(jumnuan)
    while index < len(jumnuan):
        dif = abt - jumnuan[index]
        if dif in jumnuan:
            jumnuan.remove(dif)
            count += 1
        else:
            index += 1
    print(count)
ped(sorted([int(input()) for _ in range(int(input()))]), int(input()))
