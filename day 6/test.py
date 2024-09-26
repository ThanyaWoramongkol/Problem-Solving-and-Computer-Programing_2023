"""B - Fully pair?"""

def pair(prepare):
    """-"""
    storage = ""
    for alp in prepare:
        if alp not in storage:
            storage += alp
    for char in storage:
        text = prepare.count(char)
        if text%2:
            print(char, end='')
pair(input())
