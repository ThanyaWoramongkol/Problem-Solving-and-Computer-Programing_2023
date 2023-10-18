"""AndAgainAndAgainAndAgainAndAgain"""

def main(sentense):
    """check sara more than 1"""
    sara = ['a', 'e', 'i', 'o', 'u']
    count = 0
    remain = []
    for i in sentense:
        if i in sara:
            for alp in i:
                if alp in sara:
                    count += 1
        if count >= 2 and not '.' in i:
            remain.append(i)
        elif count >= 2:
            remain.append(i[0:-1])
        count = 0
    if len(remain) == 0:
        print("Nope")
main(input().split())