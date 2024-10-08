# ArrayList 클래스 구현
# - 고정 크기의 스택(용량이 미리 정해진 리스트 사용)
#==============================================================================================================
class Stack :
    def __init__(self,capacity=10) :
        self.capacity = capacity
        self.items = [None]*self.capacity
        self.top = 0
        
        def size(self): return self.top
        def clear(self): self.top = 0
        
        def isEmpty(self) : return self.top == 0
        def isFull(self) : return self.top == self.capacity
        
        def push(self, item) : 
            if not self.isFull() : 
                self.items[self.top] = item
                self.top += 1
            else:
                print("overflow")
                exit()
                
        def pop(self) :
            if not self.isEmpty():
                self.top -= 1
                return self.items[self.top]
            else:
                print("underflow")
                exit()
                
        def peek(self) :
            if not self.isEmpty():
                return self.items[self.top-1]
            else : 
                print("underflow")
                exit()
                
        def display(self, msg = "Stack : ") :
            print(msg, end='=[')
            for i in range(self.top) :
                print(self.item[i],end=', ')
            print(']')
            
#=============================================================================================================
if __name__ == "__main__" :
    odd = Stack()
    even = Stack()
    for i in range(10):
        if i%2==0 : even.push(i)
        else : odd.push(i)
        
    even.display('  스택 even push 5회: ')
    odd.display('  스택 odd push 5회: ')
    
    print(' 스택 even   peek : ', even.peek())
    print(' 스택 odd   peek : ', odd.peek())
    for _ in range(2) : even.pop()
    for _ in range(3) : odd.pop()
    odd.peek()
    even.display('  스택 even pop 2회 : ')
    even.display('  스택 odd pop 3회 : ')
    
    