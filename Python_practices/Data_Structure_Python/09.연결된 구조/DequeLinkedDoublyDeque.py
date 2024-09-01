from Node import DNode

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.rear = None
        self.count = 0

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if(self.isEmpty()):
            self.front = self.rear = node
            if(self.isEmpty()):
                self.front = self.rear = node
            else :
                self.front.prev = node
                self.front = node
            self.count += 1

