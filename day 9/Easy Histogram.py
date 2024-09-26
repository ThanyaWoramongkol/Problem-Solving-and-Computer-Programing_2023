"""HorizentalHistogram"""
def sort_char(char):
    """sorted aA - zZ"""
    return char.lower(), char.isupper()

def graph(text):
    """-"""
    alp = {}
    for i in text:
        if i == ' ':
            continue
        alp[i] = alp.get(i, 0) + 1
    char = sorted(alp, key=sort_char)
    for i in char:
        print(i, '=', alp[i])
graph(input())
