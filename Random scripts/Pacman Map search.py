from RandomArray import rand2dArrayChar

N = int(input())
inActions = []
for i in range(N):
    inActions.append(list((input())))
# inActions = [["G"]]


def MergeSort(A, i, j):
    if i >= j:
        return

    m = (i + j) // 2
    MergeSort(A, i, m)
    MergeSort(A, m + 1, j)
    Merge(A, i, j, m)


def Merge(A, i, j, m):
    lc = A[i:m + 1]
    rc = A[m + 1:j + 1]

    lci = 0
    rci = 0
    sort_i = i

    while lci < len(lc) and rci < len(rc):
        if lc[lci] <= rc[rci]:
            A[sort_i] = lc[lci]
            lci += 1

        else:
            A[sort_i] = rc[rci]
            rci += 1

        sort_i += 1

    while lci < len(lc):
        A[sort_i] = lc[lci]
        lci += 1
        sort_i += 1

    while rci < len(rc):
        A[sort_i] = rc[rci]
        rci += 1
        sort_i += 1


def findx(x, k, ig):
    amt = 0
    for i in range(-1, -len(k) - 1, -1):
        if k[i] in ig:
            return amt
        elif k[i] in x:
            amt += 1
    return amt


def binsearch(Array, ignores, find):
    N = len(Array)
    amli = []
    for i in Array:
        MergeSort(i, 0, N - 1)
        amli.append(findx(find, i, ignores))
    return sum(amli)


print(binsearch(inActions, ["#", " "], ['G', "g"]))



def counter(A):
    Gs = 0
    for i in A:
        Gs += i.count("G")
    return Gs

for j in range(10000):
    for i in range(500):
        inActions = rand2dArrayChar(i, ["#", " ", "P", "G"])
        if binsearch(inActions, ["#", " "], ['G']) == counter(inActions):
            pass
        else:
            print(False)
            print(inActions)

