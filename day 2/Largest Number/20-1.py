"""Largest Number"""
def check():
    num = 0
    if lst.pop(count) > num:
        num = lst.pop(count)
    return num
    
def main(number_1, number_2, number_3):
    """_"""
    lst = []
    count = 0
    krung = 0
    lst.append(int(number_1 + number_2 + number_3))
    lst.append(int(number_1 + number_3 + number_2))
    lst.append(int(number_2 + number_1 + number_3))
    lst.append(int(number_2 + number_3 + number_1))
    lst.append(int(number_3 + number_2 + number_1))
    lst.append(int(number_3 + number_1 + number_2))
    if count <= 5:
        num_ans = check(lst[krung], lst[krung+1])
        count += 1
    print(lst)
main(input(), input(), input())
