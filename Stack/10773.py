#Stack
#Zero
import sys

stack = []
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    if n ==  0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
