"""MissingNumber"""

def number(jumnuan):
    """-"""
    search = [i+1 for i in range(jumnuan)]
    miss = []
    for _ in range(jumnuan):
        num = int(input())
        if num:
            miss.append(num)
        else:
            break
    for i in miss:
        if i in search:
            search.remove(i)
    print(*sorted(search), sep='\n')
number(int(input()))
