"""B - Fully pair?"""

def pair(prepare):
    """-"""
    storage = ""
    double = ''
    for alp in prepare:
        if alp not in storage:
            storage += alp
    for char in storage:
        text = prepare.count(char)
        if text%2:
            double += char
    if double == '':
        print("fully paired")
    else:
        print(double)

pair(input())
