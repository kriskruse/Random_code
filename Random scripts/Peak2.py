leng = int(input())
in_list = list(map(int, input().split()))
# leng = 6
# in_list = [-860, -981, -213, -47, 399, -669]


def findmax(leng, in_list):
    maxi = 0
    index = 0
    for i in range(leng):
        if in_list[i] > maxi:
            index = i
            maxi = in_list[i]
    return index


print(findmax(leng, in_list))
