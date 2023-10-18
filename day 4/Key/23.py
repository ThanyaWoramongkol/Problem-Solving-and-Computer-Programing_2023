"""Key"""

def key(number):
    """_"""
    lst = []
    plus_num = []
    key_storage = ""
    output = ""
    plus_key = 10

    for i in number:
        lst.append(int(i))
    for plus_key in range(10, 13):
        key_storage += str(lst[plus_key])
    plus = sum(lst) + int(key_storage) * 10
    if plus < 1000:
        plus += 1000
    for fourth in str(plus):
        plus_num.append(fourth)
    last_four = plus_num[len(plus_num) - 4:len(plus_num) + 1]
    for lasttime in last_four:
        output += lasttime
    print(output)

key(input())
