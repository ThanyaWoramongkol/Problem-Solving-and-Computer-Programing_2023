"""CoinChagev1"""

def coin(number):
    """-"""
    store = 0
    for i in [25, 10, 5, 1]:
        jumnuan = number // i
        number -= i * jumnuan
        store += jumnuan
    print(store)
coin(int(input()))
