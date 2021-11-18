import numpy as np

N = int(input())
inActions = list(map(int, input().split()))

# convert to np array
inActions = np.array(inActions)
listToSum = []

A = inActions[inActions > 0].sum()

print(A)
