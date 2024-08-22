# 하노이 탑
# 순환
def hanoi_tower(n, fr, tmp, to):
    global step
    if (n == 1) :
        step += 1
        print("[%3d]"% step, end='')
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        # 아래 두 줄 추가 #
        step += 1
        print("[%3d]"% step, end='')
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)

step = 0
hanoi_tower(3, 'A', 'B', 'C')
