"""Digit v2"""

def main(number):
    """-"""
    if 'thousand' in number:
        print(4)
    elif 'hundred' in number:
        print(3)
    elif 'eleven' in number or 'twelve' in number or \
    'teen' in number or 'ty' in number or 'ten' in number:
        print(2)
    else:
        print(1)

main(input())
