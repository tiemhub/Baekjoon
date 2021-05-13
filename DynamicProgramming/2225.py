#동적프로그래밍
#합분해
#n*k 크기의 이중배열을 사용하여 원하는 값을 추적
#keypoint : value[i][j] = value[i][j-1] + value[i-1][j-1]
import sys

n, k = map(int,sys.stdin.readline().split())

value = [[0]*n for _ in range(k)]

for i in range(k):
    value[i][0] = i+1
    for j in range(1,n):
        value[i][j] = value[i][j-1] + value[i-1][j]

print(value[-1][-1]%1000000000)
