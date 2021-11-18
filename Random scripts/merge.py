def Merge(A, i, j, m):
    lc = A[i:m + 1]
    rc = A[m+1:j+1]

    lci = 0
    rci = 0
    sort_i = i

    while lci < len(lc) and rci < len(rc):
        if lc[lci] <= rc[rci]:
            A[sort_i] = lc[lci]
            lci = lci + 1

        else:
            A[sort_i] = rc[rci]
            rci = rci + 1

        sort_i = sort_i + 1


    while lci < len(lc):
        A[sort_i] = lc[lci]
        lci = lci + 1
        sort_i = sort_i + 1

    while rci < len(rc):
        A[sort_i] = rc[rci]
        rci = rci + 1
        sort_i = sort_i + 1