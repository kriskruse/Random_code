import numpy as np
import sys
# from RandomArray import rand2dArrayCharWeighted

sys.setrecursionlimit(300000)

N = int(input())
inActions = []
for i in range(N):
    inActions.append(list((input())))
#
# inActions = [['#', '#', '#', '#', '#', '#', '#', '#'],
#              ['P', ' ', '#', ' ', ' ', ' ', ' ', '#'],
#              ['#', ' ', '#', ' ', '#', '#', ' ', '#'],
#              ['#', ' ', '#', ' ', ' ', '#', ' ', '#'],
#              ['#', ' ', ' ', ' ', ' ', '#', '#', '#'],
#              ['#', '#', '#', '#', ' ', '#', ' ', '#'],
#              ['#', ' ', ' ', ' ', ' ', '#', 'G', '#'],
#              ['#', '#', '#', '#', '#', '#', '#', '#']]


# inActions = [['P', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' '],
#              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
#              [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' '],
#              [' ', ' ', ' ', 'P', ' ', ' ', '#', ' ', ' ', ' '],
#              [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
#              [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '],
#              [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
#              [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#              [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#              [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 'G']]


# inActions = rand2dArrayCharWeighted(200, ["#", "G", "P", " "], [30, 3, 1, 50])
# print(np.array(inActions))


# inActions = [['#', '#', '#', '#', '#', '#', '#'],
#              ['#', 'G', ' ', ' ', ' ', ' ', '#'],
#              ['#', '#', '#', '#', '#', ' ', '#'],
#              ['#', ' ', ' ', ' ', ' ', ' ', '#'],
#              ['#', ' ', '#', '#', '#', '#', '#'],
#              ['#', ' ', ' ', ' ', ' ', ' ', 'P'],
#              ['#', '#', '#', '#', '#', '#', '#']]


# Find start and finishes
def findchars(A, char):
    A = np.array(A)

    if len(A.shape) < 2:
        rows = np.where(A == char)

        if len(rows) == 0:
            return None

        charIndexs = []

        if len(rows) <= 1:
            charIndexs = [(rows[0])][0]
        else:
            for i in range(len(rows)):
                charIndexs.append(rows[i])
        return charIndexs

    else:
        rows, cols = np.where(A == char)
        if len(rows) == 0:
            return None

        charIndexs = []

        if len(rows) <= 1:
            charIndexs = [(rows[0], cols[0])][0]
        else:
            for i in range(len(rows)):
                charIndexs.append((rows[i], cols[i]))
        return charIndexs


# Queue algo
class PQNode:

    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PQ:

    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front is None else False

    def push(self, value, priority):
        if self.isEmpty():
            self.front = PQNode(value, priority)
            return 1

        else:
            if self.front.priority > priority:
                newNode = PQNode(value, priority)
                newNode.next = self.front
                self.front = newNode
                return 1

            else:
                temp = self.front
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newNode = PQNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
                return 1

    def pop(self):
        if self.isEmpty():
            return
        else:
            self.front = self.front.next
            return 1

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.front.data

    def traverse(self):
        if self.isEmpty() == True:
            return []
        else:
            templist = []
            temp = self.front
            while temp:
                templist.append(temp.data)
                temp = temp.next
            return templist


# All for path finding
def distanceFunction(a, b):
    if len(a) < 2:
        return np.absolute(a[0] - b[0])
    else:
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def findPath(array, start, end):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: distanceFunction(start, end)}
    Queue = PQ()
    Queue.push(start, fscore[start])

    while Queue.traverse():
        current = Queue.peek()
        Queue.pop()
        # print(current,end)
        if current == end:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            attempt_g_score = gscore[current] + distanceFunction(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == "#":
                        continue
                else:
                    continue
            else:
                continue
            if neighbor in close_set and attempt_g_score >= gscore.get(neighbor, 0):
                continue
            if attempt_g_score < gscore.get(neighbor, 0) or neighbor not in [i for i in Queue.traverse()]:
                came_from[neighbor] = current
                gscore[neighbor] = attempt_g_score
                fscore[neighbor] = attempt_g_score + distanceFunction(neighbor, end)
                Queue.push(neighbor, fscore[neighbor])
    return False


def shortestNavigationString(pathlist):
    shortlen = 0
    shortestroute = []

    for i in pathlist:
        curlen = len(i)
        if shortlen == 0:
            shortlen = curlen
            shortestroute = i
        elif curlen < shortlen:
            shortlen = curlen
            shortestroute = i

    navigationstring = []

    for i in range(-1, - len(shortestroute), -1):
        xcord = shortestroute[i][0] - shortestroute[i - 1][0]
        ycord = shortestroute[i][1] - shortestroute[i - 1][1]
        cords = (xcord, ycord)

        if cords == (1, 0):
            navigationstring.append("N")
        elif cords == (-1, 0):
            navigationstring.append("S")
        elif cords == (0, 1):
            navigationstring.append("W")
        else:
            navigationstring.append("E")

    return " ".join(navigationstring)


def lengthShortestPath(pathlist):
    shortlen = 0
    shortestroute = []

    for i in pathlist:
        curlen = len(i)
        if shortlen == 0:
            shortlen = curlen
            shortestroute = i
        elif curlen < shortlen:
            shortlen = curlen
            shortestroute = i
    return len(shortestroute) - 1


def mainruntimer(arrayMap, Pacmanchar, Ghostchar):
    arrayMap = np.array(arrayMap)
    starts = findchars(arrayMap, Ghostchar)
    ends = findchars(arrayMap, Pacmanchar)
    # print("Pacmans and ghosts:   ", starts, ends)
    # print("Pacmens: ",len(starts),"  Ghosts:  ", len(ends))

    paths = 0
    routes = []
    if starts is not None and ends is not None:
        if type(ends) == tuple:

            if type(starts) is not list:
                start = tuple(starts)
                route = findPath(arrayMap, start, ends)
                if route:
                    route = route + [start]
                    route = route[::-1]
                    routes.append(route)
                    paths += 1



            else:
                for start in starts:
                    start = tuple(start)
                    route = findPath(arrayMap, start, ends)
                    if route:
                        route = route + [start]
                        route = route[::-1]

                        routes.append(route)
                        paths += 1

        else:
            for end in ends:
                if type(starts) is not list:
                    start = tuple(starts)
                    route = findPath(arrayMap, start, end)
                    if route:
                        route = route + [start]
                        route = route[::-1]
                        routes.append(route)
                        paths += 1


                else:
                    for start in starts:
                        start = tuple(start)
                        route = findPath(arrayMap, start, end)
                        if route:
                            route = route + [start]
                            route = route[::-1]

                            routes.append(route)
                            paths += 1

    return routes


# print(mainruntimer(inActions,"P","G"))
# print("Shortest navigation string:   ", shortestNavigationString(mainruntimer(inActions,"P","G")))
# print("Legnth of the shortest path:  ",lengthShortestPath(mainruntimer(inActions,"P","G")))
print(lengthShortestPath(mainruntimer(inActions,"P","G")))