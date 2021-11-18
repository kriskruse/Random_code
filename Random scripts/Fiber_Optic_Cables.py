import numpy as np
# from RandomArray import randConnectListWithWeights


# get the info in to a list
# Inlist = input().split()
# N, M = int(Inlist[0]), int(Inlist[1])
# inActions = []
# for i in range(M):
#     inActions.append(list((input().split())))

N, M = 20, 40
inActions = [['4', '1', '9012'], ['4', '3', '81619'], ['5', '1', '36517'], ['5', '3', '59167'], ['6', '4', '4415'],
             ['6', '2', '71818'], ['6', '1', '21613'], ['7', '1', '92907'], ['9', '1', '5101'], ['9', '3', '79229'],
             ['10', '3', '14777'], ['10', '7', '82107'], ['10', '2', '1204'], ['10', '1', '82884'],
             ['11', '1', '60456'], ['11', '9', '29738'], ['12', '10', '69259'], ['12', '9', '9374'],
             ['13', '3', '18638'], ['13', '1', '37277'], ['14', '6', '14912'], ['14', '2', '28961'],
             ['15', '1', '53573'], ['15', '9', '62847'], ['15', '7', '16237'], ['15', '14', '28948'],
             ['16', '8', '14365'], ['16', '9', '51350'], ['16', '7', '14855'], ['17', '1', '30820'],
             ['17', '16', '74836'], ['18', '15', '62646'], ['18', '1', '95768'], ['19', '1', '39748'],
             ['19', '5', '24997'], ['19', '10', '37534'], ['19', '12', '73511'], ['20', '7', '5080'],
             ['20', '11', '76623'], ['20', '12', '65084']]
# inActions = randConnectListWithWeights(M, N, 150, 1)
print(inActions)


def make_adjacency_matrix(neighborlist, housecount):
    matrix = np.full((housecount + 1, housecount + 1), np.nan)  # might have to be +1
    for element in neighborlist:
        house1 = int(element[0])
        house2 = int(element[1])
        cost = int(element[2])
        matrix[(house1, house2)] = cost
        matrix[(house2, house1)] = cost
    return matrix


def find_lowest_cost(adj_matrix):
    connected = np.zeros((len(adj_matrix), len(adj_matrix)))
    HousesConnected = []
    for i in range(1, len(adj_matrix)):
        HousesConnected.append(i)
        row = adj_matrix[i]
        lowestRow = np.nanmin(row)
        col = adj_matrix[:, i]
        lowestCol = np.nanmin(col)

        col_index = np.where(row == lowestRow)[0]
        connected[(i, col_index)] = lowestRow
        connected[(col_index, i)] = lowestRow

        row_index = np.where(col == lowestCol)[0]
        connected[(i, row_index)] = lowestCol
        connected[(row_index, i)] = lowestCol

    # print(HousesConnected)
    return connected


def sumcost(price_matrix):
    costlist = []
    index_number = 0
    for rows in price_matrix:
        costlist.append(sum(rows[:index_number]))
        index_number += 1
    return sum(costlist)


adj_matrix = make_adjacency_matrix(inActions, N)
lowest_cost_matrix = find_lowest_cost(adj_matrix)
cost = int(sumcost(lowest_cost_matrix))
# print(adj_matrix)
# print(lowest_cost_matrix)
print(cost)
