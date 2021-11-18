import queue

N, M = 20, 40
inActions = [[4, 1, 9012], [4, 3, 81619], [5, 1, 36517], [5, 3, 59167], [6, 4, 4415],
             [6, 2, 71818], [6, 1, 21613], [7, 1, 92907], [9, 1, 5101], [9, 3, 79229],
             [10, 3, 14777], [10, 7, 82107], [10, 2, 1204], [10, 1, 82884],
             [11, 1, 60456], [11, 9, 29738], [12, 10, 69259], [12, 9, 9374],
             [13, 3, 18638], [13, 1, 37277], [14, 6, 14912], [14, 2, 28961],
             [15, 1, 53573], [15, 9, 62847], [15, 7, 16237], [15, 14, 28948],
             [16, 8, 14365], [16, 9, 51350], [16, 7, 14855], [17, 1, 30820],
             [17, 16, 74836], [18, 15, 62646], [18, 1, 95768], [19, 1, 39748],
             [19, 5, 24997], [19, 10, 37534], [19, 12, 73511], [20, 7, 5080],
             [20, 11, 76623], [20, 12, 65084]]


def LowestCostConnection(listCon, amountBuildings):  # ,amountConPrice
    priceQueue = queue.PriorityQueue()
    connected = []
    cost = []
    conChosed = []

    for element in listCon:
        conTup = (element[0], element[1])
        conPrice = element[2]
        priceQueue.put((conPrice, conTup))

    while len(connected) < amountBuildings:
        connection = priceQueue.get()
        houses = connection[1]
        house1 = houses[0]
        house2 = houses[1]
        price = connection[0]
        ThisConnected = False

        if house1 not in connected:
            connected.append(house1)
            cost.append(price)
            ThisConnected = True

            conChosed.append(connection)

        if house2 not in connected:
            connected.append(house2)
            if not ThisConnected:
                cost.append(price)
                conChosed.append(connection)
    # print(conChosed)
    return sum(cost)


totalcost = LowestCostConnection(inActions, N)
print(totalcost)