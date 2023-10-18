"""Run Length Encoding"""

def decode(text):
    """-"""
    count = 0
    storage = ''
    output = ''
    for i in text:
        if count == 0:
            storage = i
        if storage != i:
            output += str(count) + storage
            count = 0
        storage = i
        count += 1
    return output
print(decode(input()+" "))
            