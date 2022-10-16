from itertools import product


n = 6
posActions = ["left", "right"]
actionList = list(product(posActions, repeat=int(n / 2)))
greedyScore = 0
algoScore = 0

ls=[1,2,3,4,5,6,7,8]
print(ls[1:])
print(ls[0:len(ls)-1])

