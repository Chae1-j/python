# 미로탐색 > 너비우선
from QueueCircular import CircularQueue

def isValidPos(x,y) :
    if(x < 0 or y < 0 or x >= MAZE_SiZE or y >= MAZE_SIZE) :
        return False
    else :
        return map[y][x] == '0' or map[y][x] == 'x'


def BFS() :
    q = CircularQueue()
    q.enqueue((0,1))
    print('BFS : ')

    while not q.isEmpty() :
        here = q.dequeue()
        print(here, end='->')
        x = here[0]
        y = here[1]
        if(map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue((x, y - 1))
            if isValidPos(x, y + 1) : q.enqueue((x, y + 1))
            if isValidPos(x - 1, y) : q.enqueue((x - 1, y))
            if isValidPos(x + 1, y) : q.enqueue((x + 1, y))
    return False

map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6
