# 파이썬의 함수



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