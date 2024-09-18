#---------------------------- 순환 구조 알고리즘

def search_bst(n,key) :                         # 키를 이용한 탐색
    if n == None:                               # 공백 -> 탐색 실패
        return None
    elif key == n.key:                          # 같으면 -> 탐색 성공
        return n
    elif key < n.key:                           # 키가 작으면 -> 왼쪽 서브 트리
        return search_bst(n.left,key)
    else:                                       # 키가 크면 -> 오른쪽 서브 트리
        return search_bst(n.right,key)

#---------------------------- 반복 구조 알고리즘
def search_bst_iter(n,key) :
    while n != None :
        if key == n.key :
            return n
        elif key < n.key :
            n = n.left
        else:
            n = n.right
    return None

# >>>>>>> 위 함수 2개는 키를 이용한 탐색

# 값을 이용한 탐색 : 전위 순회
def search_value_bst(n, value) :
    if n == None: return None
    elif value == n.value: return n
    res = search_value_bst(n.left,value)
    if res is not None: return res
    return search_value_bst(n.right,value)


def insert_bst(r,n) :
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else :
            return insert_bst(r.left,n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else :
            return insert_bst(r.right,n)
    else:
        return False


# ======================================================
class BSTNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

# 최대와 최소 노드 탐색
#탐색 알고리즘- 최소 노드 탐색
def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

# 최대 노드 탐색
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n



def delete_bst_case1(parent,node, root) :
    if parent is None:
        root = None
    else :
        if parent.left == node :
            parent.left = None
        else :
            parent.right = None
    return root

def delete_bst_case2(parent, node, root) :
    if node.left is not None :
        child = node.left
    else :
        child = node.right
    if node == root :
        root = child
    else :
        if node is parent.left :
            parent.left = child
        else : parent.right = child
    return root

def delete_bst_case3(parent, node, root) :
    succp = node
    succ = node.right
    while succ.left is not None :
        succp = succ
        succ = succ.left

    if(succp.left == succ) :
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value

    return root

def delete_bst(root,key): # 전체 삭제 알고리즘
    if root == None: return None
    parent = None
    node = root
    while node != None and node.key != key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right
    if node == None : return None

    if node.left == None and node.rigth == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None :
        root = delete_bst_case2(parent, node, root)
    else :
        root = delete_bst_case3(parent, node, root)
    return root


class BSTMap() :
    def __init__(self):
        self.root = None

    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)

    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)
    def search(self, key): return search_value_bst(self.root, key)

    def searchValue(self, key): return search_value_bst(self.root, key)

    def insert(self,key,value=None):
        n = BSTNode(key,value)
        if self.isEmpty() : self.root = n
        else : insert_bst(self.root,n)

# 강의 19회차 완료