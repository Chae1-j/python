# 1. 람다함수
"""
이름이 없기 때문에 익명함수라고도 한다.
"""
# 2. 재귀함수
"""
파이썬 일정기간 반복하여 자기자신 호출할 경우 오류 발생!
> 종료 조건이 필요하다!!

"""
# 재귀 함수 작성
# def factorial(n) :
#     return n*factorial(n-1)
# print(factorial(15)) # 종료조건이 없어 Recursion 오류 발생

def factorial(n) :
    if n == 0:
        return 1
    return n*factorial(n-1)
print(factorial(15))

# 위 함수를 람다 함수로 변환
fact = lambda x: x==0 and 1 or x*fact(x-1)
print(fact(15))

# 구구단 출력 실습 : 람다 함수와 리스트 내포를 활용해 2단부터 9단까지....
print([(lambda x,y : '{} X {} = {}'.format(x,y,x*y))(x,y) for x in range(2,10) for y in range(1,10)])

#------------------------------------------실습------------------------------------------------------
# 1. 한 줄의 람다 함수로 변경
"""
def func(a):
    if a > 10 :
        return 'a가 10보다 크다'
    else :
        return 'a가 10보다 작다'
print(func(14))"""
print((lambda a: 'a가 10보다 크다' if a>10 else 'a가 10보다 작다')(14)) # lambda뒤에 매개변수 전달

# 2. map 함수와 람다 함수 활용
"""
def func(a):
    l=[]
    for i in range(a):
        l.append(i**2)
    return l
print(func(5))
"""
print(list(map((lambda a : a**2),range(5))))