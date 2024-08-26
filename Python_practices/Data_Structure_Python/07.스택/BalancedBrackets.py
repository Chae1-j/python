# 괄호검사 알고리즘 테스트
# - 괄호검사 : 스택의 응용 
#==========================================================================================================
from stackClass import Stack

def checkBrackets(statement) :
    stack = Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty() :
                return False
            else: 
                left = stack.pop()
                if(ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                        (ch == ")" and left != "(") :
                        return False
                        
    return stack.isEmpty()