'''
간단한 정렬 알고리즘 : 선택정렬, 삽입정렬, 버블정렬
> 보다 더 효율적인 정렬 알고리즘 
- 병합정렬 : 분할 정복 기법. 연속적 분할과 병합을 이용
- 퀵정렬, 이중 피벗 퀵정렬 : 분할정복 기법, 피벗을 이용한 정렬
- 힙정렬 : 제자리 정렬로 구현하는 방법법
키값을 비교하지 않고 분배를 이용하는 정렬 : 기수정렬, 카운팅 정렬' > 키값에 제한이 있음

* 분할 정복 전략(Divide and Conquer)
- 문제를 보다 작은 2개의 문제로 분리하고 각 문제를 해결한 다음, 결과를 모아서 원래의 문제를 해결
- 대표적인 정렬알고리즘
    - 분할과정 : 리스트를 두개의 부분 리스트로 나눔. 균등 분하
    - 정복과정: 리스트의 항목이 하나 > 이미 정복된 것
    - 병합과정 : 정복된 부분 리스트를 병함. 효율적인 병합 알고리즘이 필요
* 병합 정렬 알고리즘
- 리스트를 균등 분할
- 분할된 부분 리스트를 순환적으로 정렬
- 정렬된 부분 리스트의 병합 과정이 중요요

* 병합 정렬의 시간복잡도
- 비교횟수 : log(n)개의 패스
- 이동횟수 : 2n * log(n)
 > O(n log n)

'''

def merge(A, left, mid, right) : # 병합 알고리즘
    global sorted
    k = left
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]
            j, k = j + 1, k + 1
    # 한쪽에 남아 있는 레코드의 일괄복사
    if i > mid : sorted[k : k+right-j+1] = A[j:right + 1]
    else : sorted[k:k+mid-i+1] = A[i:mid + 1]
    # 배열 sorted의 리스트를 배열 list[]로 다시 복사
    A[left:right+1] = sorted[left:right+1]
    
# 병합 정렬 알고리즘을 이용해 배열을 오름차순으로 정렬
def merge_sort(A, left, right) :
    if left < right :                   # 항목의 수가 두 개 이상인 경우
         mid = (left + right) // 2      # 리스트의 균등 분할
         merge_sort(A, left, mid)       # 부분 리스트 정렬
         merge_sort(A, mid+1, right)    # 부분 리스트 정렬
         merge(A, left, mid, right)     # 병합

sorted = []

def testAllSort() :
    org = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    global sorted
    sorted = list(org)
    data = list(org)
    print("Original : ", data)
    merge_sort(data, 0, len(data) - 1)
    print("MergeSort : ", data)

testAllSort()
