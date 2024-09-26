"""MAC"""
def alpha(text):
    """store"""
    store = ""
    for i in text:
        if i.isalpha():
            store += i
    return store

def invalid(store):
    """error"""
    char = ["A", 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
    error = False
    for i in store:
        if i in char:
            continue
        error = True
        break
    return error

def address(physical):
    """-"""
    store = ""
    error = False
    output = ''
    store = alpha(physical)
    error = invalid(store)

    if '-' in physical and (not error) \
    and len(physical.replace("-", "")) == 12:
        lst = physical.split('-')
        for i in lst:
            if len(i) == 2:
                continue
            error = True
        output = "VALID 1"
    elif ':' in physical and (not error) \
    and len(physical.replace(":", "")) == 12:
        lst = physical.split(':')
        for i in lst:
            if len(i) == 2:
                continue
            error = True
        output = "VALID 2"
    elif '.' in physical and (not error) \
    and len(physical.replace(".", "")) == 12:
        lst = physical.split('.')
        for i in lst:
            if len(i) == 4:
                continue
            error = True
        output = "VALID 3"
    else:
        error = True

    if error or output == '':
        print("ERROR")
    else:
        print(output)

address(input())
