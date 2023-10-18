"""LastStand"""
import json

def last(lst):
    """-"""
    for i in lst:
        print(i % 10)

last(json.loads(input()))
