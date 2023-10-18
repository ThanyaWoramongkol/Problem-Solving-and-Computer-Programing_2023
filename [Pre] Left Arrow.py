"""_"""
def main(jumnuan, height):
    """_"""
    start = 1
    count = height//2
    if height == 1:
        print(jumnuan * "*")
    else:
        while True:
            if height < 0:
                break
            print(height // 2 * " ", end="")
            print(jumnuan * "*")
            height -= 2
        while True:
            print(start * " ", end="")
            print(jumnuan * "*")
            start += 1
            if start-1 == count:
                break
main(int(input()), int(input()))
