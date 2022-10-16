from itertools import  product


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
        cards = cards[0:len(cards)-1]
    return score, cards


def actionPhase(cards, action):
    score, cards = updateList(action, cards)
    updateList(takeGreedy(cards[0],cards[-1]),cards)
    return score, cards

def mainGame(n,cards):
    tempCards = cards
    scoreList = []
    algoScore = 0
    posActions = ["left", "right"]
    actionList = list(product(posActions, repeat=int(n / 2)))

    for actionPairs in actionList:
        cards = tempCards
        for action in actionPairs:
            score, cards = actionPhase(cards, action)
            algoScore += score
        scoreList.append(algoScore)

    return max(scoreList)


if __name__ == "__main__":
    n, cards = inFromCommand()
    print(mainGame(n, cards))


