# 파이썬의 함수
"""
함수는 입력 값으로 어떤 일을 수행한 뒤 결과값을 얻는 것 > 반복된 코드를 일반화함
시용법 :
def 함수명(매개변수) :
    코드
"""


#-------------------------------------------실습---------------------------------------------------
#매개변수는 3개(숫자1, 숫자2, 연산)
#연산의 기본 매개변수는 덧셈
# 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈

def cal(a,b,c):
    if c == 0 :
        return a + b
    elif c == 1 :
        return a - b
    elif c == 2 :
        return a * b
    elif c == 3 :
        return a / b
    else :
        return None

cal(1,2,3)

# 2. 가변 매개변수 활용. 입력받은 단을 모두 출력하는 구구단 함수로 변경
def gugudan(a):
    for i in range(1,10):
        print("{} X {} = {}".format(a,i,a*i))

gugudan(5)