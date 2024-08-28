# 큐 ADT 구현 : 원형 큐의 구현
class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.items = [None] * capacity

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1)%self.capacity

    def clear(self):
        self.front = self.rear

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.front] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%self.capacity]

    def display(self, msg='Queue :'):
        print(msg, end=' = [')
        count = self.size()
        for i in range(count):
            print(self.items[(self.front+1+i)%self.capacity], end=', ')
        print("]")

#=========================================================================================
if __name__ == '__main__':
    print('원형큐 테스트')
    q = CircularQueue()
    for i in range(9):
        q.enqueue(i)
    q.display('     enqueue()x9')
    print('     enqueue()-->', q.dequeue())
    print('     enqueue()-->', q.dequeue())
    print('     enqueue()-->', q.dequeue())
    q.display('     dequeue()x3:    ')

    q.enqueue('홍길동')
    q.enqueue('이순신')
    q.enqueue('강감찬')
    q.display('     dequeue()x3:    ')
    print('     enqueue()-->', q.dequeue())
    q.display('     dequeue()x1:   ')
    print('     peek()-->', q.peek())