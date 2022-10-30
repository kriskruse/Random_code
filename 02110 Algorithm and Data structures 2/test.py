from math import ceil
from itertools import product


def inFromCommand():
    return int(input()), list(map(int, input().split()))


def takeGreedy(left, right):
    return "left" if left > right else "right"


def updateList(action, cards):
    # Update the list
    if action == "left":
        score = cards[0]
        cards = cards[1:]
    else:
        score = cards[-1]
        cards = cards[0:len(cards) - 1]
    return score, cards


def actionPhase(cards, action):
    score, cards = updateList(action, cards)
    if len(cards) < 1:
        return score, cards
    _, cards = updateList(takeGreedy(cards[0], cards[-1]), cards)
    return score, cards


def mainGame(n, cards):
    originalCards = cards
    scoreList = []
    posActions = ["left", "right"]
    sampleLen = ceil(n / 2)
    actionList = list(product(posActions, repeat=sampleLen))

    for actionPairs in actionList:
        cards = originalCards
        algoScore = 0
        for action in actionPairs:
            score, cards = actionPhase(cards, action)
            algoScore += score
        scoreList.append(algoScore)
    return max(scoreList)


if __name__ == "__main__":
    n, cards = inFromCommand()
    print(mainGame(n, cards))
