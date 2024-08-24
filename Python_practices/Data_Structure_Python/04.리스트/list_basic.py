# ㅍㅏ이썬 리스트 기본 활용
#=============================================================================================================

A = []
B = [1, 2, 3, 4]
c = ["hi", "list"]

print("len(A) = ", len(A))
print("len(B) = ", len(B))
print(B[1], B[1])
print("B = ", B)

sum = 0
for i in range(len(B)):
    sum = sum + B[i]

print("sum(B) = ", sum)