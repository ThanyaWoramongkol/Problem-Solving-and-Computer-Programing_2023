"""HorizentalHistogram"""
def more(output):
    """if - > 5"""
    count = 0
    for _ in range(output):
        if count == 5:
            print("|", end='')
            count = 0
        if count >= 0:
            print("-", end='')
            count += 1

def graph(text):
    """-"""
    alp = {i for i in text if i.islower()}
    upper = {j for j in text if j.isupper()}
    char = sorted(alp) + sorted(upper)
    for i in char:
        output = text.count(i)
        print(i, ": ", end="")
        if output <= 5:
            print("-" * output)
        else:
            more(output)
            print()
        #print(output)
graph(input())
