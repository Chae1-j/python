class Entry:
    def __init__(self, key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("\t%s:%s" % (self.key, self.value))

class BinaryMap:
    def __init__(self):
        self.table = []                         # 엔트리 저장을 위한 테이블(리스트)

    def size(self):
        return len(self.table)

    def display(self, msg):
        print(msg)
        for entry in self.table:
            print(entry)

    def search(self, key):                  # 이진 탐색
        pos = binary_search(self.table, key, 0, self.size() - 1)
        if pos >= 0:                        # 탐색 성공: 인덱스
            return self.table[pos]
        else :                              # 탐색 실패: -1
            return None

    def insert(self, key, value):
        pos = 0
        while pos < self.size() :                   # 삽입 위치 찾는 과정
            if self.table[pos].key >= key:
                break
            pos += 1

        self.table.insert(pos, Entry(key, value))

    def delete(self , key):
        # 삭제할 키값을 가진 엔트리의 인덱스 찾기 : 이진탐색
        pos = binary_search(self.table, key, 0, self.size() - 1)
        if pos >= 0:
            self.table.pop(pos)

    # 이진탐색 - 순환
    def binary_search(A, key, low, high):
        if(low <= high):                    # 하나 이상의 항목이 있어야 탐색
            middle = (low + high) // 2
            if(key == A[middle].key) :       # 탐색성공
                return middle
            elif(key < A[middle].key) :     # 왼쪽 부분리스트 탐색
                return A.binary_search(A, key, low, middle - 1)
            else:
                return binary_search(A, key, middle + 1, high)

        return -1

    def binary_search_iter(A, key, low, high):
        while(low <= high):
            middle = (low + high) // 2
            if key==A[middle].key :
                return middle
            elif (key > A[middle].key) :
                low = middle + 1