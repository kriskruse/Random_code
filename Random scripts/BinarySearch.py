A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def BinarySearch(A, i, j, x):
    if j < i:
        return False
    m = int((i + j) / 2)
    if A[m] == x:
        return True
    elif A[m] < x:
        return BinarySearch(A, m + 1, j, x)
    else:
        return BinarySearch(A, i, m - 1, x)


print(BinarySearch(A, 0, 9, 18))
