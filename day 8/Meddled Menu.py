"""Meddled Menu"""

def restuarant():
    """-"""
    lst = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "CLOSED":
            del lst[0:]
            break
        if menu == "SOMETHING'S WRONG":
            del lst[0:]
        elif "Can't do:" in menu:
            lst.remove(menu[menu.index(":")+2:])
        else:
            if menu[int(menu.index("#")+1):] == "N":
                lst.append(menu[:menu.index(" #")])
            else:
                lst.insert(int(menu[menu.index("#")+1:]) - 1, menu[:menu.index(" #")])
    print("Full Course:", lst, "Reversed:", lst[::-1])
restuarant()

