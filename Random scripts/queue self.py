N = int(input())
inActions = []
for i in range(N):
    inActions.append((input().split()))

queue = []
def enq(x):
    queue.append(x)

def deq():
    print(queue[0])
    queue.remove(queue[0])


for i in inActions:
    if i[0] == "E":
        enq(i[1])
    if i[0] == "D":
        deq()