# 예외의 종류와 예외 처리
'''
1. 프로그래밍 언어의 오류
- 구문 오류(Syntax Error)
- 논리적 오류(Logical Error)/ 런타임 오류(Runtime Error) : 프로그램 실행 중에 발생하는 오류.
    문법적으로 틀린것이 없으므로 즉시 인식되지 않음.


* 예외 처리 방법
1. try, except 구문
    - try : (예외 발생 가능한) 일반적인 수행문들
    - except : 예외가 발생하였을 때 수행문들
    > 예외를 그냥 넘어가고 싶은 경우 pass 키워드 사용
2. try, except, else 구문
    - else를 붙여서 사용하면, 예외가 발생하지 않았을 때 실행할 코드를 지정할 수 있음
3. try, except, else, finally 구문
    - try, except, else 뒤에 finally를 붙여서 사용하면, 예외 발생 유무에 관계 없이 실행되는 코드를 작성할 수 있음.

>> try 구문은 단독으로 사용할 수 없음
>> else 구문은 반드시 except 구문 뒤에 와야 함

* 예외 객체와 예외 구분
1. 예외 객체 : 예외가 발생하면, 예외와 관련된 정보가 생성(예외 객체로 활용 가능)
2. 예외 구분 : 예외 객체를 활용해 조건문처럼 예외 종류에 따라 다른 코딩을 할 수 있음.
3. 예외 구분의 잘못된 예 :
    - 예외 처리의 순서(예외의 포함 관계) : Arithmetic > ZeroDivision, Overflow, FloatingPoint
4. 강제로 예외 발생시키기 : raise
'''


#--------------------------------------실습-----------------------------------------------------
# 정수를 입력 받아 구구단 출력> 숫자아닐때 예외처리 9보다 클때는 9단 츨력 1이 입력되었을 땐 2단
a = input()
try :
    if(a.isdigit()) :
        a = int(a)

    if(a > 9) :
        a = 9
    elif(a < 2) :
        a = 2
    else:
        a = a
    for i in range(1,20):
        print("{} X {} = {}", format(a, i, a*i))
except Exception as msg :
    print(msg)