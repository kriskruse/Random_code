import random


# generate a random array
def randarray(N, lower, upper):  # N Define the size of the array
    A = []
    for i in range(N):
        num = random.randint(lower, upper)
        A.append(num)
    # print(A)
    return A


def randarraychar(N, char):
    A = []
    for i in range(N):
        A.append(char[random.randint(0, len(char) - 1)])
    return A


def rand2dArrayChar(N, char):
    A = []
    for i in range(N):
        A.append(randarraychar(N, char))
    return A


def randArrayCharWeighted(N, chars, weights):
    A = []
    weightedlist = []
    num = 0
    for char in chars:
        weightedlist += [char] * weights[num]
        num += 1
    for i in range(N):
        A.append(weightedlist[random.randint(0, len(weightedlist) - 1)])
    return A


def rand2dArrayCharWeighted(N, chars, weights):
    A = []
    for i in range(N):
        A.append(randArrayCharWeighted(N, chars, weights))
    return A


def randConnectListWithWeights(lenList, ConnectIDhigh, weightHigh, ConnectIDlow=0, weightLow=0):
    if ConnectIDhigh == ConnectIDlow:
        return False
    A = []
    for i in range(lenList):
        ConnectId1 = random.randint(ConnectIDlow, ConnectIDhigh)
        ConnectId2 = random.randint(ConnectIDlow, ConnectIDhigh)
        while ConnectId1 == ConnectId2:
            ConnectId2 = random.randint(ConnectIDlow, ConnectIDhigh)

        sublist = [ConnectId1, ConnectId2, random.randint(weightLow, weightHigh)]
        A.append(sublist)
    return A
