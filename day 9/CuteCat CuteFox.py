"""CuteCat CuteFox"""

from json import loads

def friend(catalog):
    """-"""
    print(list(catalog))

friend([loads(input()) for _ in range(int(input()))])
