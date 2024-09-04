# LinearProbMap
class Entry :
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%$:%$"%(self.key, self.value))

    class LinearProbMap:
        def __init__(self, M):
            self.table = [None] * M
            self.M = M

    def hashFn(self, key):
        return key % self.M

    def insert(self, key, value):
        id = self.hashFn(key)
        count = self.M
        while count > 0 and(self.table[id] != None and self.table[id] != 1) :
            id = (id + 1 + self.M) % self.M
            count -= 1

            if count > 0 :
                self.table[id] = Entry(key, value)

            return

    def search(self , key):
        id = self.hashFn(key)
        count = self.M
        while count > 0 :
            if self.table[id] == None : return None
            if self.table[id] != -1 and self.table[id].key == key:
                return self.table[id]
            id = (id + 1 + self.M) % self.M
            count -= 1
        return None

    def delete(self, key):
        id = self.hashFn(key)
        count = self.M
        while count > 0 :
            if self.table[id] == None : return None
            if self.table[id] != -1 and self.table[id].key == key:
                self.table[id] = -1
                return
            id = ( id + 1 + self.M) % self.M
            count -= 1

    def display(self, msg):
        print(msg,end='')
        for e in self.table :
            if e == None : print("  x  ",end='')
            elif e == -1 : print("  o  ",end='')
            else: print("%3d"%e.key, end='')
        print()

# 군집화 > 이차조사법(Quadratic Probing) : 바로 다음 위치가 아니라 제곱
# 이중 해싱법 : 재해싱, 다른 해시 함수를 이용해 다음 위치 계산