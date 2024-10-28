""" 
다익스트라 > 시작 정점에서 다른 모든 정점까지의 최단경로 거리 계산하는 알고리즘. 탐욕적 기법 사용
개념
- dist[v] : S내의 정점만을 거쳐서 다른 정점 v로 가는 최단 거리
- 확정된 최단거리가 있을 때 거리가 확정된 정점 중(dist) 가장 작은것을 탐욕적으로 선택함
- 간선의 가중치는 음수여서는 안됨.

* 필요자료
- dist[] : 시작 정점으로부터의 거리 > 최초: 시작 정점과의 간선의 가중치
- found[] : 거리가 확정되었는지 여부 > 최초 : 시작 정점만 True, 나머지는 False
- path[] : 이전 정점의 인덱스

* 시간 복잡도 : O(n^2) n의 제곱
> 주 반복문을 n번 반복
> 내부 반복문을 2n번 반복
> 모든 정점 쌍의 최단 경로를 구하려면 n번 반복 -> O(n^3)
"""
def shortest_path_dijkstra(vertex, adj, s) :
    vsize = len(vertex)
    dist = list(adj[s])
    path = [s] * vsize
    found = [False] * vsize
    found[s] = True
    
    for i in range(vsize-1) :
        print("Step%2d: "%(i+1), dist)
        u = choose_vertex(dist, found) 
        found[u] = True
        
        for w in range(vsize) :
            if not found[w] :
                if(dist[u] + adj[u][w] < dist[w]) :
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
    return path

def choose_vertex(dist, found) : # 임시 > 코드 수정 예정
    return 0

# 테스트 프로그램
INF = 999
vertex = ['A','B','C','D','E','F','G']
weight = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, 13, 5],
          [10, 6, INF, 9, 13, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)