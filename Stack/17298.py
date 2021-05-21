#Stack
#오큰수
#index를 stack에 넣는다.
#오큰수를 찾지 못한 index는 stack에 넣은후 while을 통해 탐색 및 초기화를 반복
import sys

n = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
stack = []
result = [-1]*n

for i in range(n):
    try:
        while A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
    except:
        pass
    stack.append(i)

for i in range(n):
    print(result[i],end=' ')

    
