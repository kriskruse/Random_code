N, W = input().split()
A = list(map(int, input().split()))
N = int(N)
W = int(W)

# N,W = 8 , 15
# A = [2,5, 3, 1, 8, 4, 5, 7]

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


MergeSort(A,0,N)

cur_weight = 0
stones = 0
for i in A:
    if cur_weight + i <= W:
        cur_weight += i
        stones +=1
    else: break
print(stones)