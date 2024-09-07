#=================================================================================================================
print(5/2, ', ',5//2)

class Tnode :
    def __init__(self,elem, left=None, right=None):
         self.elem = elem
         self.left = left
         self.right = right

    def isLeaf(self) :
        return self.left is None and self.right is None

def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def testBinaryTree():
    print("\n====================이진트리 테스트=================================================")
    d = Tnode('D',None,None)
    e = Tnode('E',None,None)
    b = Tnode('B',d,e)
    f = Tnode('F',None,None)
    c = Tnode('C',f,None)
    root = Tnode('a',b,c)

    print('\n In-Order : ', end='')

testBinaryTree()



# 노드의 개수
def count_node(n):
    if n is None:           # 공백 노드이면 (종료조건)
        return 0
    else:                   # 공백 노드가 아니면(순환 호출)
        return 1 + count_node(n.left) + count_node(n.right)

# 단말 노드의 수
def count_leaf(n):
    if n is None: return 0
    elif n.isLeaf(): return 1       # 단말노드이면 1반환
    else: return count_leaf(n.left) + count_leaf(n.right)   # 순환 호출

# 트리의 높이
def calc_height(n):
    if n is None: return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1