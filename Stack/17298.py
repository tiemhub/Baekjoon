#Stack
#오큰수
import sys

n = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))


for i in range(n):
    result = -1
    for j in A[i+1:]:
        if j > A[i]:
            result = j
            break
        
    print(result,end=" ")
    
