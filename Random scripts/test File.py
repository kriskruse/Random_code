import sys
from RandomArray import rand2dArrayCharWeighted

sys.setrecursionlimit(300000)

# N = int(input())
# inActions = []
# for i in range(N):
#     inActions.append(list((input())))


#
# inActions = [['#', '#', '#', '#', '#', '#', '#', '#'], ['P', ' ', '#', ' ', ' ', ' ', ' ', '#'], ['#', ' ', '#', ' ', '#', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', '#', 'G', '#'], ['#', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', '#', '#', '#', ' ', '#', ' ', '#'], ['#', 'G', ' ', ' ', ' ', '#', 'G', '#'], ['#', '#', '#', '#', '#', '#', '#', '#']]


def findPacman(A, Pacman):
    firstindex = 0
    secoundindex = 0
    for i in A:
        if i.count(Pacman) > 0:
            secoundindex = i.index(Pacman)
            return [firstindex, secoundindex]
        else:
            if firstindex >= len(A) - 1:
                return None
            firstindex += 1


def findGhosts(A, Ghost):
    firstindex = 0
    secoundindex = 0
    found = []
    for i in A:
        numGhost = i.count(Ghost)
        if numGhost == 1:
            secoundindex = i.index(Ghost)
            found.append([firstindex, secoundindex])
        elif numGhost > 1:
            for j in range(numGhost):
                secoundindex = i.index(Ghost)
                i[secoundindex] = "F"
                found.append([firstindex, secoundindex])
        if firstindex >= len(A) - 1:
            return found
        else:
            firstindex += 1


def findneighbors(A, index):
    neighbour = []
    neighbourcells = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for i in neighbourcells:
        if len(A) - 1 >= index[0] + i[0] >= 0 and len(A) - 1 >= index[1] + i[1] >= 0:
            neighbour.append([index[0] + i[0], index[1] + i[1]])
    return neighbour


def validspot(A, index, wall, V):
    if A[index[0]][index[1]] == wall or index in V:
        return False
    else:
        return True


def pathfinder(A, step, end, wall, distance, visited):
    visited.append(step)
    if step == end:
        return distance
    else:
        for i in findneighbors(A, step):
            if validspot(A, i, wall, visited):
                returned = pathfinder(A, i, end, wall, distance + 1, visited)
                if returned is not None:
                    return returned


def pathtoghost(A, wall, Ghost, Pacman):
    ghostWithPath = 0
    paccord = findPacman(A, Pacman)
    ghosts = findGhosts(A, Ghost)
    for i in ghosts:
        if pathfinder(A, i, paccord, wall, 0, []) is not None:
            ghostWithPath += 1
    return ghostWithPath


A = rand2dArrayCharWeighted(10, ["#", "G", "P", " "], [10, 1, 1, 20])

# print(pathtoghost(inActions, "#", "G", "P"))
