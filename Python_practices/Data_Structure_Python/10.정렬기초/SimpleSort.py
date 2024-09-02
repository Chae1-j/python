import random

def printStep(arr, val) :
    print("    Step %2d = " % val, end ='')
    print(arr)
    
# 선택 정렬 함수
def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if(A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]         # 배열 항목 교환
        printStep(A, i + 1)                     # 중간 과정 출력용 문장
        
        
#===========================================================================================
# 테스트 데이터
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("   Original : ", data)
selection_sort(data)
print("Selection : ", data)