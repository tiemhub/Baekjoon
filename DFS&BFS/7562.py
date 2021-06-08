#DFS&BFS
#나이트의 이동
import sys
from collections import deque

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    visited = [[False]*n for _ in range(n)]

    start = list(map(int,sys.stdin.readline().split()))
    end = list(map(int,sys.stdin.readline().split()))

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    done = False
    times = -1

    while queue and not done:

        for _ in range(len(queue)):
            i,j = queue.popleft()

            if [i,j] == end:
                done = True
                break
            
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]

                if 0 <= x < n and 0 <= y < n:
                    if not visited[x][y]:
                        visited[x][y] = True
                        queue.append([x,y])

        times += 1

    if done:
        print(times)
    else:
        print(-1)

            
