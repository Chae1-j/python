# 문자열의 특징, 메소드 등을 활용하여 특정 문자 뽑아내기
s = "Today is July 12, 2024. Tomorrow is July 13, 2024"
print(s)

print(s.split('.'))
tmp = s.split('.')[0]
print(tmp)

# 문자열 포맷팅 활용
# 구구단 2단 실행하기
# @ x @ = @
print("{} X {} = {}".format(2,1,2)) 
print("{} X {:f} = {}".format(2,2,4))
print("{} X {} = {:2}".format(2,3,6))  