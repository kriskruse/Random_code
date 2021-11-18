import queue as qu

priq = qu.PriorityQueue()

ln = [(1,"hus 8"),(2,"hus 2"),(4,"hus 3"),(9,"hus 5"),(7,"hus 4")]


for element in ln:
    priq.put(element)



while not priq.empty():
    print(priq.get())