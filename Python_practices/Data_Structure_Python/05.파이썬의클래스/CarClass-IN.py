# SuperCar Class 만들기
# - 생성자
# - 멤버함수 재정의(overriding)
#=====================================================================
# 클래스 정의
class Car :
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def display(self):
        print(self.color, ":" , self.speed)

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def isEqual(self, carB):
        if self.color == carB.color :
            return True
        else :
            return False

    def __eq__(self, carB):         # a == b 로 비교
        if self.color == carB.color :
            return True
        else:
            return False
    # 자동 문자열 변환 str() 함수
    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)

# Car를 상속한  SuperCar클래스 만들기
class SuperCar(Car) :
    def __init__(self, color, speed = 0,bTurbo = True):
        super().__init__(color, speed)
        # super > 부모클래스의 생성자 내 안에 있는 부모
        self.bTurbo = bTurbo # 나한테만 있는...!

        def speedUp(self):
            if self.bTurbo :
                self.speed += 30 # bTurbo가 켜져 있으면 이걸 실행
            else:
                super().speedUp() # bTurbo가 꺼져 있으면 부모클래스 함수 실행
        # > 메서드 재정의!!

sCar = SuperCar("blackpink", 0, False)
print("sCar : ", sCar)
sCar.speedUp()
sCar.speedUp()
print("sCar : ", sCar)