"""Binary"""

def banary(number):
    """-"""
    return str(number) if number in [0, 1] else banary(number//2) + str(number%2)
print(banary(int(input())))
