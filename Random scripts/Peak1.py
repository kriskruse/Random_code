# leng = int(input())
# in_list = list(map(int, input().split()))
leng = 6
in_list = [-860, -981, -213, -47, 399, -669]


def findmax(liste, length):
    for i in range(length):
        try:
            up = liste[i+1]
        except:
            up = 0

        down = -99999999999999999999999
        if i-1 >= 0:
            down = liste[i-1]

        if down <= liste[i] >= up:

            index = i
            break
    return index


print(findmax(in_list, leng))
