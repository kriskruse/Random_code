
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


link = LinkedList()
print(link)

# Create a linkedlist using the above funktions
nodeone = Node("A")
link.head = nodeone
print(link)
nodetwo = Node("B")
nodethree = Node("C")
nodeone.next = nodetwo
nodetwo.next = nodethree
print(link)



