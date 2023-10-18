"""Largest Number"""

def check(lst, krung, storage):
    """_"""
    if lst[krung] > storage:
        storage = lst[krung]
        return storage
    else:
        return storage

def main(number_1, number_2, number_3):
    """_"""
    lst = []
    krung = 0
    storage = 0
    lst.append(int(number_1 + number_2 + number_3))
    lst.append(int(number_1 + number_3 + number_2))
    lst.append(int(number_2 + number_1 + number_3))
    lst.append(int(number_2 + number_3 + number_1))
    lst.append(int(number_3 + number_2 + number_1))
    lst.append(int(number_3 + number_1 + number_2))
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    if True:
        storage = check(lst, krung, storage)
        krung += 1
    print(storage)
main(input(), input(), input())
