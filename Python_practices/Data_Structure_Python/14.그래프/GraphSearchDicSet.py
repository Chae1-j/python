# 깊이 우선 탐색 알고리즘 - 순환구조 알고리즘
def dfs(graph, v, visited) :
    if v not in visited:
        visited.add(v)
        print(v, end='')
        nbr = graph[v] - visited

        for u in nbr :
            dfs(graph, u, visited)

# 너비우선탐색 알고리즘 - 큐를 사용하여 구현
import collections
def bfs(graph, start) :
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        print(v, end='')
        nbr = graph[v] - visited
        for u in nbr :
            visited.add(u)
            queue.append(u)


mygraph = { "A" : {"B","C"},
            "B" : {"A","D"},
            "C" : {"A","D","E"},
            "D" : {"B","C","F"},
            "E" : {"C","G","H"},
            "F" : {"D"},
            "G" : {"E","H"},
            "H" : {"B",""}
            }

print('DFS : ', end='')
dfs(mygraph, "A", set())
print()

print('BFS : ', end='')
bfs(mygraph, "A")
print()
