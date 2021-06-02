#DFS & BFS
#미로 탐색
import sys

def bfs(i,j):
    
    visited[i][j] = 1
    queue = [[i,j]]
    cnt = 1

    while queue:

        i,j = queue[0]
        del queue[0]

        if i == n-1 and j == m-1:
            return cnt
        
        if i != 0:
            if visited[i-1][j] == 0 and line[i-1][j] == '1':
                queue.append([i-1,j])
                visited[i-1][j] = 1
        if j != 0:
            if visited[i][j-1] == 0 and line[i][j-1] == '1':
                queue.append([i,j-1])
                visited[i][j-1] = 1
        if i != n-1:
            if visited[i+1][j] == 0 and line[i+1][j] == '1':
                queue.append([i+1,j])
                visited[i+1][j] = 1
        if j != m-1:
            if visited[i][j+1] == 0 and line[i][j+1] == '1':
                queue.append([i,j+1])
                visited[i][j+1] = 1

        cnt += 1
    
n, m = map(int,sys.stdin.readline().split())
line = [0]*n
visited = [[0]*m for i in range(n)]

for i in range(n):
    line[i] = sys.stdin.readline().strip()

print(bfs(0,0))
