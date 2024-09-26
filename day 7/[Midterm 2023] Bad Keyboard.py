"""Bad Keyboard"""

def keycap(text):
    """-"""
    output = ""
    for i in text:
        if i == "o":
            output += "i"
        elif i == "i":
            output += "o"
        elif i == "O":
            output += "I"
        elif i == "I":
            output += "O"
        else:
            output += i
    return output
print(keycap(input()))
