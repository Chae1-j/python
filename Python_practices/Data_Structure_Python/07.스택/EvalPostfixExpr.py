from stackClass import Stack
def evalPostfix(expr) :
    s = Stack()
    for token in expr :
        val2 = s.pop()
        val1 = s.pop()
        if(token == '+') : s.push(val1 + val2)
        elif(token == '-') : s.push(val1 - val2)
        elif(token == '*') : s.push(val1 * val2)
        elif(token == '^') : s.push(val1 ** val2)
    else:
        s.push(float(token))
    return s.pop()

#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('스택의 응용2 : 후위표기실 계산 \n')

    expr1 = ['8','2','/','3','-','3','2','*','+']
    expr2 = ['1','2','/','4','-','1','4','*','+']
    str3 = ' 8 2 / 3 -3 2 * +'
    expr3 = str3.split()

    print(expr1, '---->', evalPostfix(expr1))
    print(expr2, '---->', evalPostfix(expr2))
    print(expr3, '---->', evalPostfix(expr3))