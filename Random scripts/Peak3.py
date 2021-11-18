leng = int(input())
in_list = list(map(int, input().split()))

def peak(A, I, J):
    m = int((I + J) / 2)
    # get neighbors
    if m < leng - 1:
        up = A[m + 1]
    else:
        up = A[m] - 1

    if m - 1 > -1:
        down = A[m - 1]
    else:
        down = A[m] - 1

    # check for peak
    if up <= A[m] >= down:
        return m
    elif down > A[m]:
        return peak(A, I, m - 1)
    elif up > A[m]:
        return peak(A, m + 1, J)


print(peak(in_list, 0, leng - 1))
