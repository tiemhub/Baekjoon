#DFS&BFS
#벽 부수고 이동하기
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

maze = [0]*n
visited = [[False]*m for _ in range(n)]

for i in range(n):
    maze[i] = sys.stdin.readline().strip()

end = False
times = 0
queue = deque()
queue.append([0,0,False]) #i,j,벽을 부쉈는가(boolean)
visited[0][0] = True

while queue and not end:

    for _ in range(len(queue)):
        i,j, brk = queue.popleft()

        if (i,j) == (n-1,m-1):
            end = True
            break

        if i != n-1:
            if not visited[i+1][j]:
                if maze[i+1][j] == '1' and not brk:
                    visited[i+1][j] = True
                    queue.append([i+1,j,True])
                elif maze[i+1][j] == '0':
                    visited[i+1][j] = True
                    queue.append([i+1,j,brk])
        if j != m-1:
            if not visited[i][j+1]:
                if maze[i][j+1] == '1' and not brk:
                    visited[i][j+1] = True
                    queue.append([i,j+1,True])
                elif maze[i][j+1] == '0':
                    visited[i][j+1] = True
                    queue.append([i,j+1,brk])
        if i != 0:
            if not visited[i-1][j]:
                if maze[i-1][j] == '1' and not brk:
                    visited[i-1][j] = True
                    queue.append([i-1,j,True])
                elif maze[i-1][j] == '0':
                    visited[i-1][j] = True
                    queue.append([i-1,j,brk])
        if j != 0:
            if not visited[i][j-1]:
                if maze[i][j-1] == '1' and not brk:
                    visited[i][j-1] = True
                    queue.append([i,j-1,True])
                elif maze[i][j-1] == '0':
                    visited[i][j-1] = True
                    queue.append([i,j-1,brk])

    times += 1

if end:
    print(times)
else:
    print(-1)
