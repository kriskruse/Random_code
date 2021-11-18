from RandomArray import randarray


# A = array, i = left_index, j = right_index, m = middel,
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


# A = randarray(15,0,16)
A = ["P","G","#","#","#"]
l = len(A) - 1
MergeSort(A, 0, l)
print(MergeSort(A, 0, l))
print(A)
