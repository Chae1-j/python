'''
개념
- 모든 정점 사이의 최단경로거리를 찾는 알고리즘
- Floyd-Warshall알고리즘이라고도 함
- 동적 계획(Dynamic Programming)전략을 이용
- 아이디어 :
    > 모든 정점 사이의 최단 경로 거리를 구하려면 모든 정점을 거치는 상황을 고려
    > 어떤 정점을 하나도 거치지 않는(바로 가는) 경로에서부터 시작
    > 정점을 하나씩 순차적으로 고려했을 때 경로를 개시
    > 최종적으로 정점을 고려한 경로 거리를 수정
    

- 그래프의 인접 행렬 표현 W -> D
- 아무 정점도 고려하지 않은 상태에서 최종적으로 n개의 정점을 모두 고려했을 때의 최단 경로 거리를 구하는 것이 핵심
'''

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)
    
    A = list(adj)
    for i in range(vsize):
        A[i] = list(adj[i])
        
    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
        print(A)
        
    # 인접행렬 adj를 A에 복사... 깊은복사(deepcopy())를 이용할 수 있음.
    
#테스트 프로그램
INF = 999
vertex = ['A','B','C','D','E','F','G']
weight = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, 13, 5],
          [10, 6, INF, 9, 13, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]
print("Shortest Path By Floyd Algorithm")
shortest_path_floyd(vertex, weight)