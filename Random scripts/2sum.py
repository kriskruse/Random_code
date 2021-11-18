# A = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, -3]
from RandomArray import randarray
A = randarray(15, -10, 10)
N = len(A)


def twosum(A, N):
    bol = False
    for i in A:
        for j in range(N):
            if i + A[j] == 0:
                bol = True
                return bol
    return bol

def threesum(A, N):
    bol = False
    for i in A:
        for ii in A:
            for j in range(N):
                if i + ii + A[j] == 0:
                    print(i, ii , A[j])
                    bol = True
                    return bol
    return bol


print(threesum(A, N))
