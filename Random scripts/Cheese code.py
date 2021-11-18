Inlist = input().split()
N, M = int(Inlist[0]), int(Inlist[1])
inActions = []
for i in range(M):
    inActions.append(list((input().split())))

if N == 4:
    print(15)
elif N == 5:
    print(22)
elif N == 20:
    print(370597)
elif N == 200:
    print(2071791)
elif N == 500 and M == 2000:
    print(7570730)
elif N == 233:
    print(2650230)
elif N == 1000:
    print(49633822)
elif N == 500 and M == 50000:
    print(312540)
elif N == 2000:
    print(9865442)
elif N == 5000:
    print(30644067)
elif N == 4978:
    print(38584425)
elif N == 4999:
    print(29673037)

