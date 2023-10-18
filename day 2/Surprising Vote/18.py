"""SurprinsingVote"""

def main(total, maxi):
    """_"""
    mini = total - maxi * 2
    if mini < maxi - 2 and maxi > 2:
        print("Surprising")
    else:
        print("Not surprising")

main(float(input()), float(input()))
