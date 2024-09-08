# 순환 구조 알고리즘

# 반복 구조 알고리즘
def search_bst_iter(n,key) :
    while n != None :
        if key == n.key :
            return n

