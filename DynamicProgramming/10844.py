#동적계획법
#계단수 찾기
import sys
    
n = int(sys.stdin.readline().strip())

stnum = [9,17] + [0]*98
fibo = [1,2] + [0]*98

for i in range(2,n):
    fibo[i] = fibo[i-1] + fibo[i-2]
    stnum[i] = stnum[i-1]*2 - fibo[i-1]

print(stnum[n-1])
