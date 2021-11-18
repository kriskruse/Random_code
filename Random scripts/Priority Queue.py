class PriorityQueueNode:

    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:

    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front is None else False

    def push(self, value, priority):
        if self.isEmpty():
            self.front = PriorityQueueNode(value, priority)
            return 1

        else:
            if self.front.priority > priority:
                newNode = PriorityQueueNode(value, priority)
                newNode.next = self.front
                self.front = newNode
                return 1

            else:
                temp = self.front
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
                return 1

    def pop(self):
        if self.isEmpty():
            return

        else:
            self.front = self.front.next
            return 1

    def peek(self):

        if self.isEmpty():
            return
        else:
            return self.front.data

    def traverse(self):
        if self.isEmpty() == True:
            return
        else:
            templist = []
            temp = self.front
            while temp:
                templist.append(temp.data)
                # print(temp.data, end=" ")
                temp = temp.next
            return templist

# Driver code
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.push((3, 4), 6.222)
    pq.push((3, 3), 7)
    pq.push((3, 2), 4)
    print(pq.peek())
    print(pq.traverse())
