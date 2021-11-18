CH = list(map(int, input().split()))

A = CH[0]
L = CH[1]
O = CH[2]
something = 0
if A < L and A < O:
    print("Anna")
    something = 1

if L < A:
    print("Laura")
    something = 1

if O < A or O < L:
    print("Oscar")
    something = 1

if something != 1:
    print("NONE")