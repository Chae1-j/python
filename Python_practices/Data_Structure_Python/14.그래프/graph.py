def printDegree_AM(graph) :
    vlist = graph[0]
    M = graph[1]
    for i in range(len(vlist)):
        row = M[i]
        count = 0
        for e in M[i]:
            if e > 0: count += 1
        print(vlist[i], ":", count, end=" ")
    print()

print('AM : ' , end='')
printDegree_AM(graph)

vertex = ['A','B','C','D','E','F','G','H']
adjList1 = [

]

def printDegree_AL1(graph):
    vlist = graph[0]
    alist = graph[1]
    for i in range(len(vlist)):
        count = len(alist[i])
        print(vlist[i], ":", count, end=" ")
    print()

graph3= {'A': ['B','C']
         ,'B': ['A','D']
         ,'C': ['A','D','E']
         ,'D': ['B','C','F']
         }

def printDegree_AL2(graph):
    for v in graph:
        count = len(graph[v])

        print(v, ":", count, end=" ")
    print()

print('AL2: ', end='')
printDegree_AL2(graph3)

def printDegree_AL3(graph):
    for v in graph:
        count = len(graph[v])

        print(v, ":", count, end=" ")
    print()

print('AL3: ', end='')
printDegree_AL3(graph3)