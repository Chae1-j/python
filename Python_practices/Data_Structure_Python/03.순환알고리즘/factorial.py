# 팩토리얼 함수(순환 구조와 반복 구조)
#=============================================================================================================================

# 순환구조 Factorial
def factorial(n) :
    if n == 1 :
        return 1
    else :
        return (n * factorial(n-1))
    
print('Factorial tnsghks(3) = ', factorial(3))

# 반복구조 Factorial
def factorial_iter(n) :
    result = 1
    for k in range(n, 0, -1) :
        result = result * k
    return result

#=============================================================================================================================
print('Factorial 순환(3) = ', factorial(3))
print('Factorial 반복(3) = ', factorial_iter(3))

#=============================================================================================================================
import time
print("순환 구조(2**500) = ", factorial(500))
print("반복 구조(2**500) = ", factorial_iter(500))

t1 = time.time()
for i in range(100000) :
    factorial(500)
t2 = time.time()
for i in range(100000) :
    factorial_iter(500)
t3 = time.time()

print("순환구조...", t2-t1)
print("반복구조...", t3-t2)