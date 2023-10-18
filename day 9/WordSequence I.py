"""WordSequence I"""

def drawing(text):
    """-"""
    col = 1
    for _ in range(len(text)):
        print(text[:col])
        col += 1
drawing(input())
