#Stack
#균형잡힌 세상
#열린 괄호를 스택에 넣고 닫힌 괄호 때마다 연산하기
import sys

while True:
    string = sys.stdin.readline().rstrip()
    end = False
    stack = []
    
    if string == '.':
        break

    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                end = True
                break
            
            if stack.pop() == '(':
                pass
            else:
                end = True
                break
        elif i == ']':
            if len(stack) == 0:
                end = True
                break
            
            if stack.pop() == '[':
                pass
            else:
                end = True
                break

    if len(stack) != 0:
        end = True

    if end:
        print('no')
    else:
        print('yes')
