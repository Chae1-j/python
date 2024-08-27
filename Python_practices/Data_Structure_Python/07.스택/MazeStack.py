from stackClass import Stack
map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6

def isvalidPos(x, y) :      # (x,y)가 갈 수 있는 방인지 검사하는 함수
    if x < 0 or y< 8 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False        #(x,y)가 미로 밖이면 -> 갈 수 없음
    else :                  # 출구(x)이거나 방(g))이면 갈 수 있음
        return map[y][x] == '0' or map[y][x] == 'x'
def DFS() :
    stack = Stack()         # 깊이우선탐색 함수
    stack.push ((0,1))      # 사용할 덱 객체를 준비
    print('DFS:')           # 후단에 시작위치 삽입. (0,1)은 튜플

    while not stack.isEmpty() :     # 공백이 아닐 동안
        here = stack.pop()          # 후단에서 항목을 꺼냄
        print(here, end='->')
        (x,y) = here
        #x = here[0];               # 튜플은 (x,y)임. 따라서 here[0]
        # y = here[1];              # here[1]이 y
        if(map[y][x] == 'x'):       #  출구이면 성공. True 반환
            return True
        else :
            map[y][x] = '.'         # 현재위치를 지나왔다고 '.' 표시
            # 4방향의 웃을 검사해 갈 수 있으면 덱 후단에 삽입
            if isvalidPos(x - 1, y): stack.push((x - 1, y)) # 좌
            if isvalidPos(x + 1, y): stack.push((x + 1, y)) # 우
            if isvalidPos(x, y - 1): stack.push((x, y - 1)) # 상
            if isvalidPos(x, y + 1): stack.push((x, y + 1)) # 하
    return False

result = DFS()
if result : print('--> 미로탐색 성공')
else : print('--> 미로탐색 실패')