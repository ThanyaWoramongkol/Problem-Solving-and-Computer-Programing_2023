"""HorizentalHistogram"""
def sort_char(char):
    """sort aA-zZ"""
    return char.lower(), char.isupper()

def graph(text):
    """-"""
    alp = []
    for i in text:
        if i in alp or i == ' ':
            continue
        else:
            alp.append(i)
    char = sorted(alp, key=sort_char)
    for i in char:
        print(i, '=', text.count(i))
graph([i for i in input()])
