"""Future Message"""
def main(text):
    """is... = True"""
    if text.isdecimal():
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    else:
        print("Other")
main(input())
        