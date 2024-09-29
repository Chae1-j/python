
def dfs_cc(graph, colour, v, visited):
    if v not in visited :
        visited.add(v)
        colour.append(v)
        nbr = graph[v] - visited
        for u in nbr:
            dfs_cc(graph, colour, u, visited)
            
            
def find_connected_component(graph) :
    visited = set()
    colourList = []
    
    for vtx in graph :
        if  vtx not in visited :
            color = []
            dfs_cc(graph, color, vtx,visited)
            colourList.append(color)

            print("그래프 연결성분 개수 = %d" % len(colourList))
            print(colourList)

mygraph = { "A" : set(["B", "C"]),
            "B" : set(["A"]),
            "C" : set(["A"]),
            "D" : set(["E"]),
            "E" : set(["D"])
            }
print('find_connected_component : ')
find_connected_component(mygraph)