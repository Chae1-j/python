from xml.dom.NodeFilter import NodeFilter
from Node import Node

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def size(self):
        return self.count

    def clear(self):
        self.top = None
        self.count = 0


    def isEmpty(self):
        return self.top == None

    def isFull(self):
        return False

    def push(self, item):
        self.top = Node(item, self.top)
        self.count += 1

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def pop(self):
        if not self.isEmpty():
            self.count -= 1
            data = self.top.data
            self.top = self.top.link
            return data

    def display(self, msg = "Stack : "):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end='')
            node = node.link
        print()

    def size1(self):
        node = self.top                 # top에서부터
        cnt = 0                         # 항목의 수 초기화
        while not node == None:         # 유효한 노드이면
            node = node.link            # 링크를 따라 움직임
            cnt += 1                    # 항목의 수 증가
        return cnt                      # 항목의 수 반환

#===========================================================================================
if __name__ == '__main__':
    print('<연결된 구조로 구현한 스택 테스트>')
    odd = LinkedStack()
    even = LinkedStack()
    for i in range(10):
        if i%2 == 0: even.push(i)
        else: odd.push(i)

    even.display('  스택 even     peek : ')
    odd.display('  스택 odd     peek : ')

    print('  스택 even     peek : ', even.peek())
    print('  스택 odd     peek : ', odd.peek())
    for _ in range(2) : even.pop()
    for _ in range(3) : odd.pop()
    odd.peek()
    even.display('  스택 even pop 2회: ')
    even.display('  스택 odd pop 3회: ')

