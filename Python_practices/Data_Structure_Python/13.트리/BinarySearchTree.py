# 순환 구조 알고리즘
def search_bst(n,key) :                         # 키를 이용한 탐색
    if n == None:                               # 공백 -> 탐색 실패
        return None
    elif key == n.key:                          # 같으면 -> 탐색 성공
        return n
    elif key < n.key:                           # 키가 작으면 -> 왼쪽 서브 트리
        return search_bst(n.left,key)
    else:                                       # 키가 크면 -> 오른쪽 서브 트리
        return search_bst(n.right,key)


# 반복 구조 알고리즘
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


