import random


def getcard(amount):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cardtogo = []
    for i in range(amount):
        card = random.choice(cards)
        cardtogo.append(card)
    return cardtogo

