#DFS&BFS
#벽 부수고 이동하기
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

maze = [0]*n
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maze[i] = sys.stdin.readline().strip()

end = False
times = 0
queue = deque()
queue.append([0,0,0]) #i,j,벽을 부쉈는가(boolean)
visited[0][0] = [True, True]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
while queue and not end:

    for _ in range(len(queue)):
        i,j, brk = queue.popleft()

        if (i,j) == (n-1,m-1):
            end = True
            break

        for k in range(4):

            x = i + dx[k]
            y = j + dy[k]

            if 0 <= x < n and 0 <= y < m:
                if maze[x][y] == '1' and (not brk) and (not visited[x][y][1]):
                    visited[x][y][0] = True
                    queue.append([x,y,1])
                elif maze[x][y] == '0' and not visited[x][y][brk]:
                    visited[x][y][brk] = True
                    queue.append([x,y,brk])
                    

    times += 1

if end:
    print(times)
else:
    print(-1)
