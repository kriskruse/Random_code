from RandomArray import randarray

A = randarray(150000)
n = len(A)

def insertionSort(A, n):
    for i in range(n):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return A


print(insertionSort(A, n))
