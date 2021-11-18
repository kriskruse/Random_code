N = int(input())
inActions = []
for i in range(N):
    inActions.append((input().split()))

stack = []


def push(x):
    stack.append(x)


def pop():
    print(stack[-1])
    stack.remove(stack[-1])


for i in inActions:
    if i[0] == "PU":
        push(i[1])
    if i[0] == "PO":
        pop()
