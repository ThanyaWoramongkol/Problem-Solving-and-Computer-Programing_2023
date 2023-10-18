"""LineSorting"""
def agibar(sortors):
    """sort number by len"""
    return len(sortors)


def linear(agiba):
    """agiba"""
    print(*sorted(agiba, key=agibar), sep="\n")

linear([input() for _ in range(int(input()))])
