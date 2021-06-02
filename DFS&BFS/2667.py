#DFS&BFS
#단지번호붙이기
import sys

def dfs(i,j):

    cnt = 1
    visited[i][j] = 1

    if i != 0:
        if visited[i-1][j] == 0 and line[i-1][j] == '1':
            cnt += dfs(i-1,j)
    if j != 0:
        if visited[i][j-1] == 0 and line[i][j-1] == '1':
            cnt += dfs(i,j-1)
    if i != n-1:
        if visited[i+1][j] == 0 and line[i+1][j] == '1':
            cnt += dfs(i+1,j)
    if j != n-1:
        if visited[i][j+1] == 0 and line[i][j+1] == '1':
            cnt += dfs(i,j+1)

    return cnt
    

n = int(sys.stdin.readline().strip())
line = [0]*n
visited = [[0]*n for i in range(n)]
result = []

for i in range(n):
    line[i] = sys.stdin.readline().strip()

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and line[i][j] == '1':
            result.append(dfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)
            
