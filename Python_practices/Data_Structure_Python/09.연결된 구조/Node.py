#

# Singly Linked Node.
class Node:
    def __init__(self, elem, link):
        self.data = elem
        self.link = link
# Doubly Linked Node
class DNode :
    def __init__(self, elem, prev, next):
        self.data = elem
        self.prev = prev
        self.next = next
