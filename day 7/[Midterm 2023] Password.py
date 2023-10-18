"""Password"""
from string import punctuation
import math

def password(text):
    """-"""
    lower = 0
    upper = 0
    number = 0
    punc = 0
    for i in text:
        if i.isalpha():
            if i.isupper():
                upper = 26
            elif i.islower():
                lower = 26
        elif i.isdecimal():
            number = 10
        elif i in punctuation:
            punc = 32
    roll = lower + upper + number + punc
    enthopy = math.floor(math.log2((roll) ** len(text)))
    print(enthopy)
    if enthopy >= 128:
        print("Very Strong")
    elif enthopy >= 60:
        print("Strong")
    elif enthopy >= 36:
        print("Reasonable")
    elif enthopy >= 28:
        print("Weak")
    else:
        print("Very Weak")
password(input())
