"""RecursiveFunction"""

def main(jumnuan):
    """-"""
    if jumnuan == 0:
        return 0
    elif jumnuan == 1:
        return 1
    else:
        return main(jumnuan-1) + main(jumnuan-2)
print(main(int(input())))
