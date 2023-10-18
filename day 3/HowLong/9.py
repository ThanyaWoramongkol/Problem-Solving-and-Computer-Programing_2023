"""HowLong"""

def main(number):
    """_"""
    jumnuan = 0
    if number < 0:
        for _ in str(number):
            jumnuan += 1
        jumnuan -= 1
    else:
        for _ in str(number):
            jumnuan += 1
    print(jumnuan)
main(int(input()))
