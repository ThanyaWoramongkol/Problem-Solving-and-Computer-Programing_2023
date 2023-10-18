"""Backward"""

def main():
    """-"""
    lst = []
    while True:
        text = input()
        if text == "NULL":
            break
        lst.append(text)
    print(*lst[::-1], sep="\n")
main()
