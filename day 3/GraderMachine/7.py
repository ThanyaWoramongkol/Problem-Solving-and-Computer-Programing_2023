"""GradeMachine"""

def main(start, stop):
    """append %2 == 0"""
    passed = "pass :"
    summary = 0
    if stop > start:
        for i in range(start, stop + 1):
            if i % 2 == 0:
                passed += " %d" % i
                summary += i
    else:
        for i in range(start, stop - 1, -1):
            if i % 2 == 0:
                passed += " %d" % i
                summary += i
    print("%s\nSum : %s" % (passed, summary))

main(int(input()), int(input()))
