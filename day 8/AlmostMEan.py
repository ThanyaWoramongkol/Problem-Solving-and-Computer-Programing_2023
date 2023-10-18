"""AlmostMean"""

def point(overall):
    """-"""
    kanaen = []
    remain = 0
    for i in range(len(overall)):
        kanaen.append(float(overall[i][1]))
    average = sum(kanaen) / len(kanaen)
    kanaen.sort()
    for i in kanaen:
        nearest = min(abs(i - average), abs(average - remain))
        remain = i
    print(nearest)
point([input().split() for _ in range(int(input()))])