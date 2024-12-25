'''
** 기수 정렬(Radix Sort)
- 레코드를 비교하지 않고 분배하여 정렬 수행
- 비교 기반 정렬의 하한인 O(n log n)보다 좋을 수 있음
- 시간 복잡도(n)

- 단순히 자릿수에 따라 숫자를 bucket에 넣었다가 꺼내면 정렬
- Bucket은 Queue로 이루어짐(FIFO)
- 여러 자릿수의 기수 정렬 :
    낮은 자릿수 분류 > 순서대로 읽음 > 높은 자릿수 분류

* 기수정렬의 특징
- 버킷(큐)의 개수는 키의 표현 방법과 밀접한 관계가 있음

'''

from collections import deque

def radix_sort(A):
    queues = []
    for i in range(BUCKETS) :
        queues.append(deque())

    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) :
            queues[(A[i]//factor)%10].append(A[i])

        i = 0
        for b in range(BUCKETS) :
            while queues[b] :
                A[i] = queues[b].popleft()
                i += 1
        factor *= 10
        print("step", d+1, A)

# 테스트 프로그램
import random

BUCKETS = 10
DIGITS = 4

org = []
for i in range(10) :
    org.append(random.randint(1,9999))

data = list(org)
radix_sort(data)
print("Radix : ", data)