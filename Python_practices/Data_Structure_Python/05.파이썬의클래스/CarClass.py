# 파이썬에서 Car클래스 만들기
# - 클래스의 정의, 생성자, 멤버함수 만들기
# - 객체 생성 및 활용
#=================================================================================================
# 클래스 정의
class Car:
    # 생성자 함수 : 데이터 멤버 정의 및 초기화
    def __init__(self, color, speed = 0):
        # self : this포인터의 개념과 유사. 자기자신의 멤버변수도 self를 통해서 입력
        self.color = color
        self.speed = speed

    def display(self):
        print(self.color, ":" , self.speed)

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10
    # ** 파이썬에서는 항상 self가 있어야 한다!! **


# 클래스의 사용방법
# > 객체생성
black = Car('black', 0)
red = Car('red', 120)
yellow = Car('yellow', 30)
blue = Car('blue')
green = Car('green')

black.display()
red.display()
yellow.display()
blue.display()
green.display()

green.speedUp()
green.speedUp()
green.speedUp()
green.display()