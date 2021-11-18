import numpy as np

# N = int(input())
# Lab = np.empty((0, N))
#
# for i in range(N):
#     t = np.array(list(input()))
#     Lab = np.vstack((Lab, t))

start = [0, 0]
N = 3
Lab = np.array([["A", "B", "B"], ["A", "A", "B"], ["A", "B", "A"]])


def DFS(s):
    time = 0
    last = []
    return DFS_vis(s, time, last)


def DFS_vis(v, time, last):
    vTime = time + 1
    last.append(v)
    done = False

    if v == [N - 1, N - 1]:
        print(vTime)
        done = True

    # naboer i, op, ned, venstre, højre
    neighbor = []

    if v[0] - 1 >= 0:
        neighbor.append((v[0] - 1, v[1]))
    else:
        neighbor.append(None)

    if v[0] + 1 <= N - 1:
        neighbor.append((v[0] + 1, v[1]))
    else:
        neighbor.append(None)

    if v[1] - 1 >= 0:
        neighbor.append((v[0], v[1] - 1))
    else:
        neighbor.append(None)

    if v[1] + 1 <= N - 1:
        neighbor.append((v[0], v[1] + 1))
    else:
        neighbor.append(None)

    if not done:
        for i in neighbor:
            if i != None and list(i) not in last:
                if Lab[i] != Lab[tuple(v)]:
                    DFS_vis(list(i), vTime, last)

DFS(start)
