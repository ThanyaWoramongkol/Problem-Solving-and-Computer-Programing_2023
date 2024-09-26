"""MissingNumber"""

def number(jumnuan):
    """-"""
    search = {i+1 for i in range(jumnuan)}
    miss = set()
    for _ in range(jumnuan):
        num = int(input())
        if num:
            miss.add(num)
        else:
            break
    print(*(miss ^ search), sep='\n')
number(int(input()))
