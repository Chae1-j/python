'''
** 퀵정렬
- 분할 정복기법을 사용
- 비균등 분할
- 분할을 위해 피벗을 사용
- 피벗을 제외한 좌우 부분 리스트를 순환적으로 정렬
- 병합 과정이 필요없음.
- 특징
    - 패스수 : log n
    - 시간복잡도 : O(n log n)
    - 최악의 경우 : 이미 정렬된 리스트 패스 수 : n, 시간복잡도: O(n^2)
-  불균등 완화방법이 필요

* 분할 알고리즘
- 피벗을 선택  보통 첫번째 원소
- 피벗보다 작은 항목은 피벗의 왼쪽, 큰 항목은 오른쪽
- Hoare의 분할 알고리즘
'''

def partition(A, left, right): # Hoare의 알고리즘 이용
    low = left + 1
    high = right
    pivot = A[left]
    while low < high :
        while low <= right and A[low] <= pivot : low += 1
        while low <= left and A[high] > pivot : high -= 1

        if low < high :
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high


def quick_sort(A, left, right):
    if left < right:                        # 정렬 범위가 2개 이상인 경우
        q = partition(A, left, right)       # 좌우로 분할
        quick_sort(A, left, q - 1)          # 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right)         # 오른쪽 부분리스트를 퀵 정렬

def testAllSort() :
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

    print("Original : ", data)
    quick_sort(data, 0, len(data) - 1)
    print("QuickSort : ", data)

testAllSort()