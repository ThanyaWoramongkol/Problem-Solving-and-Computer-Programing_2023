"""PickThem"""
import json

def pick(lists):
    """-"""
    lst = json.loads(lists)
    number = []
    for i in lst:
        if i % 2:
            continue
        number.append(i)
    if number == []:
        print("Nope")
    else:
        print(*number, sep="\n")

pick(input())
