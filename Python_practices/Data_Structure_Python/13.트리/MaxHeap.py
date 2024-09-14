from symbol import return_stmt


class MaxHeap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.heap = [None] * (capacity + 1)
        self.hsize = 0

    def size(self):
        return self.hsize
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.capacity


    def Parent(self, i) :
        return self.heap[i//2]
    def Left(self, i) :
        return self.heap[i*2]
    def Right(self, i) :
        return self.heap[i*2+1]

    def display(self,msg = 'Heap'):
        print(msg,self.heap[1:self.size() + 1])

    def insert(self,n) :
        self.hsize += 1
        self.heap[self.size()] = n                  # 맨 마지막 노드로 일단 삽입
        i = self.size()                             # 노드 n의 위치
        # while (i != and n > self.Parent(i)) :       # 부모보다 큰 동안 계속
        #     self.heap[i] = self.Parent(i)
        #     i = i //2
        self.heap[i] = n

    def delete(self) :
        parent = 1                                  # 루트의 인덱스
        child = 2                                   # 루트의 왼쪽 자식 인덱스
        if not self.isEmpty() :                     # 힙이 공백이 아니면 삭제 가능
            hroot = self.heap[1]                    # 삭제할 루트를 복사해 둠
            last = self.heap[self.size()]           # 마지막 노트
            while (child <= self.size()) :          # 마지막 노드 이전까지 아래로 반복
                # 만약 오른쪽 노드가 더 크면 child를 1증가(기본은 왼쪽 노드)
                if child < self.size() and self.Left(parent) < self.Right(parent) :
                    child += 1
                if last >= self.heap[child] :       # 자식이 더 작으면 : 멈춤
                    break                           # downheap종료
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.hsize -= 1
            return hroot

#===============================================================================================================
heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]

for elem in data:
    heap.insert(elem)
    heap.display('->')\


import heapq
data = [2, 5, 4, 8, 9, 3, 7, 3]
heapq.heapify(data)
print(heapq.headpop(data))