import collections

def bfsST(graph, start) :
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited
        for u in nbr:
            print("(",v,", ", u,")", end=" ")
            visited.add(u)
            queue.append(u)

# 신장트리
def topological_sort_AM(vertex, graph):
    n = len(vertex)
    inDeg = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                inDeg[j] += 1

    visit = []
    for i in range(n):
        if inDeg[i] == 0:
            visit.append(i)

    while len(visit) > 0:
        v = visit.pop()
        print(vertex[v], end='')

        for u in range(n) :
            if v != u and graph[v][u] > 0:
                inDeg[u] -= 1
                if inDeg[u] == 0:
                    visit.append(u)
# 22. 그래프 응용 위상정렬 완강