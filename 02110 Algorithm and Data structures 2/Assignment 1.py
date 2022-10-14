from functools import lru_cache

def inFromCommand():
    return int(input()), list(map(int, input().split()))

def takeGreedy(left, right):
    return "left" if left > right else "right"

def updateList(action, cards):
    # Update the list
    if action == "left":
        score = cards.pop(0)
    else:
        score = cards.pop(-1)
    return score, cards

@lru_cache(maxsize = 1000)
def takeAlgo(cards, left, right):
    if len(cards) == 2:
        action = takeGreedy(left, right)
        score, cards = updateList(action, cards)
        return score, cards
    elif len(cards) == 1:
        return updateList("right", cards)
    else:
        leftScore, leftCards = updateList("left", cards)
        rightScore, rightCards = updateList("right", cards)
        takeAlgo()


def mainGame(n,cards):
    greedyScore = 0
    algoScore = 0
    for i in range(n):
        left = cards[0]
        right = cards[-1]

        # Pick the card for the strategy
        actionAlgo = takeAlgo(cards, left, right)
        score, cards = updateList(actionAlgo, cards)
        algoScore += score

        if len(cards) < 1:
            print(algoScore)
            print(greedyScore)
            break

        # Greedy strategy takes a card
        actionGreedy = takeGreedy(left,right)
        score, cards = updateList(actionGreedy,cards)
        greedyScore += score

        if len(cards) < 1:
            print(algoScore)
            print(greedyScore)
            break

        # Keep tap on score
        # Break when no more cards


if __name__ == "__main__":
    n, cards = inFromCommand()
    mainGame(n, cards)


