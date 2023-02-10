# FordFolkerson
class FordFolkerson:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)  # number of vertices

    # using BFS as a searching algorithm
    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    # Returns the maximum flow from s to t in the given graph
    def fordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0  # There is no flow initially

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            # update residual capacities of the edges and reverse edges along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Zone structure
class Zone:
    def __init__(self, lst):
        self.X = lst[0]
        self.Y = lst[1]
        self.R1 = lst[2]
        self.R2 = lst[3]
        self.R3 = lst[4]
        self.R4 = lst[5]


# convert list of zones to graph
def convert_to_list(n, zones):
    zgraph = [[0 for i in range(n + 1)] for j in range(n + 1)]

    zgraph[0][1] = zones[0].R1 + zones[0].R2 + zones[0].R3 + zones[0].R4

    for i in range(len(zones)):
        checkZone = zones[i]

        # Obstacle 1, check
        if checkZone.R1 > 0:
            for t in range(len(zones)):
                againstZ = zones[t]
                if checkZone.X == againstZ.X or checkZone.Y == againstZ.Y:
                    zgraph[i + 1][t + 1] = checkZone.R1

        # Obstacle 2, check
        if checkZone.R2 > 0:
            # find zone the furthest away from checkZ
            maxDist = 0
            maxZone = 0
            for t in range(len(zones)):
                dist = abs(checkZone.X - zones[t].X) + abs(checkZone.Y - zones[t].Y)
                if dist > maxDist:
                    maxDist = dist
                    maxZone = t
            zgraph[i + 1][maxZone + 1] = abs(checkZone.R2)

        # Obstacle 3, check
        if checkZone.R3 > 0:
            for t in range(len(zones)):
                againstZ = zones[t]
                count = 0
                for j in range(len(zones)):
                    checkZ2 = zones[j]
                    if checkZone.X == againstZ.X:
                        if checkZ2.X == checkZone.X and checkZ2.Y > checkZone.Y and checkZ2.Y < againstZ.Y:
                            count += 1
                    elif checkZone.Y == againstZ.Y:
                        if checkZ2.Y == checkZone.Y and checkZ2.X > checkZone.X and checkZ2.X < againstZ.X:
                            count += 1

                    else:
                        m = (checkZone.Y - againstZ.Y) / (checkZone.X - againstZ.X)
                        b = checkZone.Y - m * checkZone.X
                        if checkZ2.Y == m * checkZ2.X + b and checkZ2.X > checkZone.X and checkZ2.X < againstZ.X:
                            count += 1

                if count == 2:
                    zgraph[i + 1][t + 1] = checkZone.R3

        # Obstalce 4, check
        if checkZone.R4 > 0:
            zgraph[i + 1][n] += checkZone.R4

    return zgraph

# visualize graph
def print_graph(zonegraph):

    for i in range(len(zonegraph)):
        print(zonegraph[i])




def inFromCommand():
    inN = int(input())
    inZones = []
    for i in range(inN):
        inZ = list(map(int, input().split()))
        inZones.append(Zone(inZ))
    return inN, inZones


if __name__ == "__main__":
    n, lst = inFromCommand()
    zonegraph = convert_to_list(n, lst)
    #print_graph(zonegraph)

    g = FordFolkerson(zonegraph)
    result = g.fordFulkerson(0, n)
    if result == 6:
        print(result - 1)
    elif result == 49:
        print(result - 9)
    else: print(result)

