from collections import deque

mystack = []

mystack.append("A")
mystack.append("B")
mystack.append("C")
mystack.pop()
print(mystack)

q = deque()

q.append("A")
q.append("B")
q.append("C")
print(q)
print(q.popleft())
print(q)


s = []
poplist = []

l = ["D","*","T","U","*","*","I","N","*","F","O","R","*","M","*","A","T","I","K"]

for i in l:
    if i == "*":
        poplist.append(s.pop())
    else:
        s.append(i)
print(s)
print(poplist)