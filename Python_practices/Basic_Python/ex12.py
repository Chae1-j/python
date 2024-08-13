# 사용자 정의 모듈
"""
import : 단순 코드를 가져오는 것이 아닌 가져온 코드를 실행하는 것

- 동일한 변수도 다른 모듈에서 가져와 재정의 가능
__name__ : 모듈의 이름이 저장되는 변수, 현재 모듈이 최상위 모듈로 수행되는지 여부 확인 가능
    사용자 정의 모듈에 name이 main일 때의 조건문을 적어 테스트 코드로 사용 가능
"""

#---------------------------------------------- 실습 ------------------------------------------------
# 1. random 모듈을 활용하여 1부터 45까지의 임의의 숫자 6개를 출력하는 코드 작성
# 조건 : 1. 반복문 사용 2. random 모듈의 randint 함수 사용
import random
for i in range(6) :
    print(random.randint(1,45))

# 2. random 모듈을 활용하여 로또 번호 생성기 만들기
# 중복이 없는 1 ~ 45 사이의 랜덤 번호 6개 출력/ 결과는 리스트 자료형으로 출력
l = []
for i in range(6) :
    l.append(random.randint(1,45))
    '''
    중복을 제거하는 방법
    1.
    l = []
    while True:
        temp = random.randint(1,45)
        if temp not in l:
            l.append(temp)
        if len(l) == 6:
            break
            
    2. 
    l = []
    while True:
        l.append(random.randint(1,45))
        l = set(l) # 집합자료형의 특징: 중복이 있을 수 없음 을 이용
        l = list(l)
        if len(l) == 6:
            break
    '''
l = []
while True:
    l.append(random.randint(1,45))
    l = set(l) # 집합자료형의 특징: 중복이 있을 수 없음 을 이용
    l = list(l)
    if len(l) == 6:
        break
print(l)