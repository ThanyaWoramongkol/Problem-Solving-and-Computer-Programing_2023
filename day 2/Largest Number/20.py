"""Largest Number"""
def check(num1, storage):
    if num1 > storage:
        storage = num1
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
        num_ans = check(lst[0], storage)
    if True:
        num_ans = check(lst[1], storage)
    if True:
        num_ans = check(lst[2], storage)
    if True:
        num_ans = check(lst[3], storage)
    if True:
        num_ans = check(lst[4], storage)
    if True:
        num_ans = check(lst[5], storage)
    print(num_ans)
    print(lst)
main(input(), input(), input())
