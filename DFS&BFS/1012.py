#DFS&BFS
#단지번호붙이기
import sys
        
def bfs(i,j):

    visited[i][j] = 1
    queue = [[i,j]]

    while queue:

        i,j = queue[0]
        del queue[0]
        
        if i != 0:
            if visited[i-1][j] == 0 and line[i-1][j] == 1:
                queue.append([i-1,j])
                visited[i-1][j] = 1
        if j != 0:
            if visited[i][j-1] == 0 and line[i][j-1] == 1:
                queue.append([i,j-1])
                visited[i][j-1] = 1
        if i != n-1:
            if visited[i+1][j] == 0 and line[i+1][j] == 1:
                queue.append([i+1,j])
                visited[i+1][j] = 1
        if j != m-1:
            if visited[i][j+1] == 0 and line[i][j+1] == 1:
                queue.append([i,j+1])
                visited[i][j+1] = 1
    

for _ in range(int(sys.stdin.readline().strip())):
    m, n, k = map(int,sys.stdin.readline().split())

    cnt = 0
    line = [[0]*m for i in range(n)]
    visited = [[0]*m for i in range(n)]

    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        line[y][x] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and line[i][j] == 1:
                bfs(i,j)
                cnt += 1
                
    print(cnt)
