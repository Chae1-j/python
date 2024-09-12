def dfs_cc(graph, color,v, visited):
    if v not in visited :
        visited.add(v)
        color.append(v)
        nbr = graph[v] - visited
        for u in nbr:
            dfs_cc(graph, color, u, visited)
            
            
def find_connected_component(graph) :
    visited = set()
    colourList = []
    
    for vtx in graph :
        if  vtx not in visited :
            color = []
            dfs_cc(graph, color, vtx,visited)
            colourList.append(color)