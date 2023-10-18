"""BigFrame"""

def drawing(text):
    """-"""
    storage = 0
    index = 0

    for i in range(5):
        lenght = max(storage, len(text[i]))
        storage = max(storage, len(text[i]))

    for row in range(7):
        for col in range(lenght+4):
            if row == 0 or col == 0 or col == lenght + 3 or row == 6:
                print('*', end='')
            elif col == 1:
                print(' ', end='')
                print(text[index], end=' ')
                if len(text[index]) < lenght:
                    print(' ' * (lenght - len(text[index])), end='')
                index += 1
        print()

drawing([input().strip() for _ in range(5)])
