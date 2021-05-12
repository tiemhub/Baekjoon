#동적프로그래밍
#합분해
#n*k 크기의 이중배열을 사용하여 원하는 값을 추적
import sys

n, k = map(int,sys.stdin.readline().split())

cache = [[0]*n for _ in range(k)]

for i in range(k):
    for j in range(n):
        if i == 0 or j <= i:
            cache[i][j] = 1
        
