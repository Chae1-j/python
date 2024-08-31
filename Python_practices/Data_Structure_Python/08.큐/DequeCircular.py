# 덱 ADT의 구현 : 원형 큐 클래스를 상속하여 구현
from QueueCircular import CircularQueue

class CircularDeque(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def addRear(self,item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item

    def getRear(self):
        return self.items[self.rear]

# 파이썬 collections 모듈에서 제공하는 deque 클래스
# 후단 삽입/삭제 : append/pop
# 전단 삽입/삭제 : appendleft/popleft
import collections
print('\n<파이썬 collections 모듈의 deque 테스트')
cdq = collections.deque()

for i in range(9):
    if i%2 == 0 : cdq.append(i)
    else : cdq.appendleft(i)
print("홀수(전단), 짝수(후단) 삽입 : ", cdq)

for i in range(2):
    cdq.popleft()
for i in range(3):
    cdq.pop()
print("전단 2번 후단 3번 삭제 연산:", cdq)

for i in range(9,14):
    cdq.appendleft(i)
print("전단 9~13 삽입 : ")
# ===============================================================================================
if __name__ == '__main__':
    print("<원형덱 테스트>")
    dq = CircularDeque()

    for i in range(9): 
        if i%2 == 0 : dq.addRear(i)
        else: dq.addFront(i)
    dq.display("홀수(전단), 짝수(후단) 삽입:")
    for i in range(2):
        dq.deleteFront()
    for i in range(3):
        dq.deleteRear()
    dq.display("전단 2번 후단 3번 삭제 연산:")

    for i in range(9,14):
        dq.addFront(i)
    dq.display("전단 9~13 삽입 : ")
    dq.peek()