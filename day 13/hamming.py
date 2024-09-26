"""Hamming"""

def ham(txt1, txt2):
    """-"""
    count = 0
    for i in range(len(txt1)):
        if txt1[i] == txt2[i]:
            continue
        count += 1
    return count
print(ham(input(), input()))
