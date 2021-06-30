#dp2
#내리막길
import sys

n,m = map(int,sys.stdin.readline().split())
hill = []
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

for _ in range(n):
    hill.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(m):
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if 0 <= x < n and 0 <= y < m:
                if hill[i][j] > hill[x][y]:
                    dp[x][y] += dp[i][j]

print(dp[-1][-1])
