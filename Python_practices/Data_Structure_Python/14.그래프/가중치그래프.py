def weightSum(vlist, W) :
    sum = 0
    for i in range(len(vlist)) :
        for j in range(i + 1, len(vlist)):
            if W[i][j] != None:
                sum += W[i][j]
    return sum

vertex = []
weight = 0

print('AM : weight sum =', weightSum(vertex, weight))

# 인접행렬
def printAllEdges(vlist,W) :
    for i in range(len(vlist)) :
        for j in range(i + 1, len(vlist)) :
            if W[i][j] != None and W[i][j] != 0:
                print("(%s,%s,%d" % (vlist[i], vlist[j], W[i][j]), end=' ')
    print()

printAllEdges(vertex, weight)

graphAL = {'A' : {('B',29),('F',10)         },
           'B' : {('A',29),('C',16),('G',15)},
           'C' : {('B',16),('D',12)         },
           'D' : {('C',12),('E',22),('G',16)},
           'E' : {('D',22),('F',27),('G',25)},
           'F' : {('A',10),('E',27)         },
           'G' : {('B',15),('F',10),('',0)}}

def weightSum2(graph) :
    sum = 0
    for v in graph :
        for e in graph[v]:
            sum += e[1]
        return sum // 2

print('AL : weight sum2 =', weightSum2(graphAL))

def printAllEdges2(graph) :
    for v in graph :
        for e in graph[v]:
            if v <= e[0]:
                print("(%s,%d,%d)" % (v,e[0],e[1]), end=' ')

printAllEdges2(graphAL)