# 집합 자료구조 만들기
# - 앞에서 구현한 ArrayList를 이용해 집합 자료구조를 구현함
#---------------------------------------------------------------------------------------------
from ArrayListClassBasic import ArrayList
# Set.
class Set :
    def __init__(self, capacity = 10) :     # 생성자
        self.list = ArrayList(capacity)    # 최대 항목수를 지정한 리스트

    def size(self) : return self.list.size()

    def contains(self,elem):        # elem이 원소인지 검사
        if self.list.find(elem) >= 0:
            return True
        else: return False

    def insert(self, elem):
        if not self.contains(elem):
            self.list.insert(self.size(), elem)

    def delete(self, elem):
        id = self.list.find(elem)
        if id >= 0 :
            self.list.delete(id)

    def display(self, msg) :
        self.list.display(msg)

    def clone(self):
        newSet = Set()
        for i in range(self.size()):
            newSet.insert(self.list.getEntry(i))
        return newSet

    def union(self, setB):
        newSet = self.clone()
        for i in range(setB.size()):
            newSet.insert(setB.list.getEntry(i))
        return newSet

    # 교집합
    def intersect(self, setB):
        newSet = Set()
        for i in range(self.size()):
            e1 = self.list.getEntry(i)
            for j in range(setB.size()):
                e2 = setB.list.getEntry(j)
                if e1 == e2 :
                    newSet.insert(e1)
        return newSet

    def difference(self, setB):     # C = self - B
        newSet = self.clone()
        for i in range(setB.size()):
            newSet.delete(self.list.getEntry(i))
        return newSet

setA = Set()
setA.insert('휴대폰')
setA.insert('*|₴')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB.insert('빗')
setB.insert('자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B:')

setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.insert('빗')
setB.display('Set B:')