def rotateLL(A) :
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A) :
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

#   20-1 강 27:35부터 강의 듣기
