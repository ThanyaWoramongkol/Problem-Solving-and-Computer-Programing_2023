"""IP Address"""

def ippc(address):
    """-"""
    error = False
    for i in address:
        if ' ' in i or not i.isdigit():
            error = True
            return 'Invalid IPv4 address'
    real = [int(i) for i in address]
    for i in real:
        if len(str(i)) > 3 or i > 255 or i < 0 or error:
            error = True
            break
    if not len(address) == 4:
        error = True
    if error:
        return 'Invalid IPv4 address'
    else:
        print(*real, sep='.')
        return ''
print(ippc(input().split('.')))
