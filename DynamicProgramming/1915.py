#동적프로그래밍
#가장 큰 정사각형
#1인 좌표를 저장하고 가로세로거리차가 같을 때 맥스값 갱신?
import sys

n,m = map(int,sys.stdin.readline().split())

value = []

for _ in range(n):
    value.append(list(map(int,list(sys.stdin.readline().strip()))))

dp = [[0]*(m+1) for _ in range(n+1)]
max_value = 0

for i in range(n):
    for j in range(m):
        if value[i][j]:
            dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j],dp[i][j]) +1
            max_value = max(max_value,dp[i+1][j+1])

print(max_value**2)
