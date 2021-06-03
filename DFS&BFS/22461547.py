#DFS&BFS
#토마토 3차원
import sys
from collections import deque

m, n, h = map(int,sys.stdin.readline().split())
tomato = [[[0]*m for _ in range(n)] for _ in range(h)]

cnt = 0
day = 0
queue = deque()

for i in range(h):
    for j in range(n):
        tomato[i][j] = list(map(int,sys.stdin.readline().split()))
        for k in range(m):
            if tomato[i][j][k] == 0:
                cnt +=1
            elif tomato[i][j][k] == 1:
                queue.append([i,j,k])

while queue and cnt:

    for _ in range(len(queue)):
        i,j,k = queue.popleft()

        if i != h-1 and tomato[i+1][j][k] == 0:
            tomato[i+1][j][k] = 1
            queue.append([i+1,j,k])
            cnt -= 1
        if j != n-1 and tomato[i][j+1][k] == 0:
            tomato[i][j+1][k] = 1
            queue.append([i,j+1,k])
            cnt -= 1
        if k != m-1 and tomato[i][j][k+1] == 0:
            tomato[i][j][k+1] = 1
            queue.append([i,j,k+1])
            cnt -= 1
        if i != 0 and tomato[i-1][j][k] == 0:
            tomato[i-1][j][k] = 1
            queue.append([i-1,j,k])
            cnt -= 1
        if j != 0 and tomato[i][j-1][k] == 0:
            tomato[i][j-1][k] = 1
            queue.append([i,j-1,k])
            cnt -= 1
        if k != 0 and tomato[i][j][k-1] == 0:
            tomato[i][j][k-1] = 1
            queue.append([i,j,k-1])
            cnt -= 1

    day += 1

if cnt:
    print(-1)
else:
    print(day)
        
