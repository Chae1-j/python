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
    - 리스트의 앞 쪽 절반만 처리
    - downHeap을 통해 최대 힙 조건 유지
2. 최대 힙 > 정렬 리스트트

'''

def heapSort(data) :
    heap = MinHeap()
    for n in data :
        heap.insert(n)
    for i in range(len(data)):
        data[i] = heap.delete()
        
def MinHeap() :
    print("")