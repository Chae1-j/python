# ArrayClass구현하기
# - 용량이 미리 정해진 리스트 사용
class ArrayList :
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity # 객체(데이터) : 인스턴스 변수
        self.nItems = 0 # 리스트의 현재 원소 개수

    def size(self):
        return self.nItems

    def isEmpty(self):
        return self.nItems == 0 # 공백 상태 검사
    '''
        if self.nItems == 0:
            return True
        else:
            return False
        와 같은 기능
    '''

    def isFull(self):
        return self.nItems >= self.capacity # 포화상태 검사

    def clear(self):
        self.items = [None] * self.capacity # 객체(데이터) : 인스턴스 변수
        self.nItems = 0

    def insert(self, pos, elem): # pos위치에 원소 elem 삽입
        if not self.isFull():
            for i in range(self.nItems-1, pos, -1):
                self.items[i+1] = self.items[i]
            self.items[pos] = elem
            self.nItems += 1

    def delete(self, pos):      # pos위치에 원소 제거
        if 0 <= pos < self.nItems:
            for i in range(pos, self.nItems-1):
                self.items[i] = self.items[i+1]
            self.nItems -= 1

    def append(self, elem):     # 맨 뒤에 원소 elem 삽입
        if not self.isFull():
            self.items[self.nItems] = elem
            self.nItems += 1

    def pop(self):      # 맨 마지막 원소 삭제
        if not self.isEmpty():
            self.items[self.nItems-1] = None
            self.nItems -= 1

    def getEntry(self, pos):        # pos 위치의 원소 반환
        return self.items[pos]

    def find(self, item):       # 리스트에서 item의 위치 찾기
        for i in range(self.nItems):
            if self.items[i] == item:
                return i
        return -1

    def replace(self,pos,elem):        # pos 위치의 원소 교체
        self.items[pos] = elem

    def display(self, msg='ArrayList:'):  # 리스트를 화면에 출력
        print(msg, end='=[')
        for i in range(self.nItems):
            print(self.items[i], end=', ')
            print("]")

# ============================================================================
# 이 파일이 직접 실행될 때에는 다음 문장들을 실행
# 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음
if __name__ == '__main__':
    s = ArrayList()
    s.display('클래스로 구현한 배열 구조의 리스트(ArrayList) 테스트')
    s.insert(0, 10)
    s.insert(0, 20)
    s.insert(1, 30)
    s. insert(s.size(), 40)
    s. insert(2, 50)
    s.display("클래스로 구현한 ArrayList(삽입x5): ")
    s. replace (2, 90)
    s.display("클래스로 구현한 ArrayList(교체x1): ")
    s.delete(2)
    s.delete(s.size() - 1)
    s. delete(0)
    s.display("클래스로 구현한 ArrayList(삭제×3): ")
    s. clear ()
    s.display("클래스로 구현한 ArrayList(정리후): ")