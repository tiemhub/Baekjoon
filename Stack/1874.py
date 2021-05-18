#Stack
#스택 수열
#스택을 이용해 수열 만들기
import sys

n = int(sys.stdin.readline().strip())
ptr = 0
stack = []
target = [0]*n
log = []

for i in range(n):
    target[i] = int(sys.stdin.readline().strip())

for i in range(1,n+1):
    stack.append(i)
    log.append('+')
    
    while target[ptr] == stack[-1]:
        stack.pop()
        log.append('-')
        ptr += 1
        if not stack:
            break

if not stack:
    for i in log:
        print(i)
else:
    print('NO')
