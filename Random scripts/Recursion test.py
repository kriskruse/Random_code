import math

neighbors = [[1, 1], [1, 2], [2, 1], [2, 2]]
end = [0, 1]

dis1, low1 = math.inf, math.inf
dis2, low2 = math.inf, math.inf
dis3, low3 = math.inf, math.inf
dis4, low4 = math.inf, math.inf

for i in neighbors:
    distance = math.sqrt((i[0] - end[0]) ** 2 + (i[1] - end[1]) ** 2)
    if distance < dis1:
        dis4, low4 = dis3, low3
        dis3, low3 = dis2, low2
        dis2, low2 = dis1, low1
        dis1, low1 = distance, i
    elif distance < dis2:
        dis4, low4 = dis3, low3
        dis3, low3 = dis2, low2
        dis2, low2 = distance, i
    elif distance < dis3:
        dis4, low4 = dis3, low3
        dis3, low3 = distance, i
    else:
        dis4, low4 = distance, i
sortedlist = [low1, low2, low3, low4]
print(sortedlist)
