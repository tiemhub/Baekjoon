#DFS&BFS
#토마토
import sys
from collections import deque

def bfs():
    
    queue = deque()

    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append([i,j])
                
    while queue:

        i,j = queue[0]
        del queue[0]
        
        if i != 0 and tomato[i-1][j] == 0:
            queue.append([i-1,j])
            tomato[i-1][j] = tomato[i][j] + 1
        if j != 0 and tomato[i][j-1] == 0:
            queue.append([i,j-1])
            tomato[i][j-1] = tomato[i][j] + 1
        if i != n-1 and tomato[i+1][j] == 0:
            queue.append([i+1,j])
            tomato[i+1][j] = tomato[i][j] + 1
        if j != m-1 and tomato[i][j+1] == 0:
            queue.append([i,j+1])
            tomato[i][j+1] = tomato[i][j] + 1
            

m,n = map(int,sys.stdin.readline().split())
tomato =[]

for i in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))

bfs()
result = 0
ripe = True

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            ripe = False
        result = max(result,tomato[i][j])

if ripe:
    print(result - 1)
else:
    print(-1)
            

