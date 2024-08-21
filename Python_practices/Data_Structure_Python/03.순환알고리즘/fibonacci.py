# 피보나치 수열
# ===================================================================================================================

# 순환 피보나치
def fib(n) :
    print('fib(%d)' % n)
    if n == 0 : return 0
    elif n == 1 : return 1
    else :
        return fib(n - 1) + fib(n - 2)
    
print("fib(6) = ", fib(6)) 

# 반복 피보나치
def fib_iter(n) :
    if (n < 2) : return n
    last = 0
    current = 1
    for i in range(2, n+1) :
        tmp = current
        current += last
        last = tmp
        return current