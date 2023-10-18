"""SumOfNumber"""

def main(wanted, summary):
    """_"""
    while True:
        lek = int(input())
        if lek == -1:
            break
        else:
            summary += lek
        if summary == wanted:
            break
    print(summary)

main(int(input()), 0)
