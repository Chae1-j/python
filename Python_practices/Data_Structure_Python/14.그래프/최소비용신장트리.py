# 탐욕적 기법(Greedy Method) : 그 순간에 최적을 반복적으로 선택 > 최적의 결과를 보장하는 것은 아님

# Union-Find 알고리즘
parent = []
set_size = 0

def init_set(nSets):
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id) :
    while (parent[id] >= 0) :
        id = parent[id]
    return id

def union(s1, s2) :
    global set_size
    parent[s1] = s2
    set_size = set_size -1


# Kruskal 알고리즘 구현
def MSTKruskal(vertex, adj) :
    vsize = len(vertex)
    init_set(vertex)
    eList = []

    for i in range(vsize-1) :
        for j in range(i+1, vsize) :
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))


    eList.sort(key= lambda e : e[2], reverse = True)

    edgeAccepted = 0

    while (edgeAccepted < vsize-1) :
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])

        if (uset != vset) :
            print("간선 추가 : (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted += 1

# 23-2 kruskal 최소비용 신장트리 까지 완료