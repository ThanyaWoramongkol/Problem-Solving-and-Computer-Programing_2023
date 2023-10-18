"""BootSequence"""

def main(finish):
    """_"""
    output = ""
    for i in range(1, finish):
        output += "%d_" % i
    output += str(finish)
    print(output)

main(int(input()))
