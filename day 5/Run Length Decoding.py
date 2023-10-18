"""Run Length Decoding"""

def decode(text):
    """-"""
    output = ''
    count = ''
    for i in text:
        if i.isdecimal():
            count += str(i)
        else:
            alpha = i
            output += alpha * int(count)
            count = ''
    return output
print(decode(input()) + " ")
