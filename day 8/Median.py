"""Median"""

def med(lst):
    """-"""
    if len(lst) % 2:
        print("%.1f" % lst[int(len(lst) / 2)])
    else:
        ans = (lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2
        print("%.1f" % ans)
med(sorted([int(input()) for _ in range(int(input()))]))
