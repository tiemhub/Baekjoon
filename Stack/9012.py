#Stack
#괄호
import sys


for _ in range(int(sys.stdin.readline().strip())):
    stack = list(sys.stdin.readline().strip())
    value = 0
    end = False
    while len(stack) != 0:
        temp = stack.pop()

        if temp == ')':
            value += 1
        else:
            value -= 1

        if value < 0:
            print('NO')
            end = True
            break

    if not end:
        if value != 0:
            print('NO')
        else:
            print('YES')
