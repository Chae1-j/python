'''
** 힙정렬
- 힙 : 우선순위 큐를 구현할 때 가장 효율적. 최소 heap
       모든 항목을 힙에 넣었다가 꺼내면서 나열
- 삽입 삭제 시간복잡도 > O(nlogn)
- 문제점 : 추가적인 메모리가 필요요

* 제자리 정렬로 구현한 힙 정렬
- 입력 리스트를 이용해 정렬 
1. 정렬되지 않은 리스트 > 최대 힙 : 
    - heapify
    - 리스트의 앞 쪽 절반만 처리 (뒤쪽 절반은 가족관계가 아니므로)
    - downHeap을 통해 최대 힙 조건 유지
2. 최대 힙 > 정렬 리스트트
    - 힙의 루트를 반복적으로 꺼냄 > 최댓값
    - 최댓값을 배열의 맨 뒤쪽부터 저장
    - 최대 힙의 크기가 하나 줄어듦듦

'''

def heapify(arr, n, i) :
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    # 더 큰 자식을 largest로 변경
    if l < n and arr[i] < arr[l] : largest = l
    if r < n and arr[largest] < arr[r] : largest = r
    
    if largest != i :                               # largest가 바뀌었으면 -> 교환, 순환호출
        arr[i],arr[largest] = arr[largest], arr[i] # swap
        heapify(arr, n, largest)

# def heapSort(data) :
#     heap = MinHeap()
#     for n in data :
#         heap.insert(n)
#     for i in range(len(data)):
#         data[i] = heap.delete()

def heapSort(arr) :
    n = len(arr)
    
    # 정렬되지 않은 배열 > 최대 힙
    print("i=", 0, arr)
    for i in range(n//2, -1, -1):
        heapify(arr,n,i)
        print("i=", i, arr)
    print()
    
    # 최대 힙 > 정렬된 배열열
    for i in range(n-1, 0, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i , 0)
        print("i=", i, arr)
        
arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]
heapSort(arr)
n = len(arr)
print("HeapSort: " , arr)


import heapq

arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print()