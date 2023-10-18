"""Day I"""
def main(years):
    """_"""
    if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
        print("Yes")
    else:
        print("No")
main(int(input()))
