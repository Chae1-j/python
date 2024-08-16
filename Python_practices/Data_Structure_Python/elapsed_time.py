# 실습 2-1 알고리즘의 실행시간 측정
# =======================================================================================
# 속도를 측정하고자 하는 알고리즘
def find_max(A) :
    max = A[0]
    for item in A:
        if item > max :
            max = item
    return max

# 실행시간 측정 프로그램

import time                                     # time 모듈 불러오기

array = [1, 4, 8, 3, 4, 2, 4, 5, 9, 5, 3]

start = time.time()
max = find_max(array)                           # 실행 시간을 측정하려는 코드
end = time.time()

print("최댓값 = ", max)
print("실행시간 = ", end - start)


#========================================================================================
import random

array=[random.randint(0,10000) for i in range(10000)]

#
start = time.time()
for n in range(10000):
    max = find_max(array)
end = time.time()

print("최댓값 = ", max)
print("실행시간 = ", end - start)