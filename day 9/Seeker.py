"""Seeker"""

def decode(encode):
    """-"""
    summary = 0
    remain = "0"
    number = False
    for i in encode:
        if i.isdecimal():
            remain += i
            number = True
        elif i.isalpha() and number:
            summary += int(remain)
            remain = "0"
            number = False
    summary += int(remain)
    print(summary)
decode(input())
