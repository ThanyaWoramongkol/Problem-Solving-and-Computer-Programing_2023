"""MissingCard I"""

def sumrub():
    """-"""
    deck = {'8C', 'AS', '7S', '4D', 'KD', 'KC', 'AC', 'QH', 'KH', \
    'JS', '8H', '6C', '10D', '10S', 'JD', 'QD', 'JC', '8D', \
    'QS', '2S', '7D', '5C', 'JH', '2H', '2D', '9S', '6S', '3S', \
    'KS', '4H', '7C', '9D', 'AD', '3C', '5H', '4S', '7H', '4C', \
    '6D', '6H', '3D', '9H', '5S', '9C', '10H', '8S', '10C', \
    '5D', 'QC', '2C', 'AH', '3H', 'KD'}
    card = set()
    for _ in range(51):
        card.add(input())
    now = deck.difference(card)
    for i in now:
        print(i)
sumrub()
