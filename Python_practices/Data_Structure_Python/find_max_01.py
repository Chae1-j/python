# 자료구조-1회차 : find_max0813.py

# 파이썬으로 기술한 알고리즘 : 배열에서 최대값 찾기
#==========================================================================
def find_max(A) :
    max = A[0]
    for item in A : 
        if item > max :
            max = item
    return max

# 테스트 코드
array = [20, 34, 12, 93, 84, 39, 64, 55, 24]
print("A = ", array)
print("max(A) = ", find_max(array))