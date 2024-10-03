"""
Prim의 최소비용 신장 트리
1. 그래프에서 시작 정점을 선택하여 초기 트리를 만듦
2. 현재 트리의 정점들과 인접한 정점들 중에서 간선의 가중치가 가장 작은 정점 v를 선택
3. 정점 v와 이 때의 간선을 트리에 추가
4. 모든 정점이 삽입될 때까지 2번으로 이동
"""

INF = 9999

def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrin(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        for v in range(vsize) :
            if (adj[u][v] != None) :
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

    print()