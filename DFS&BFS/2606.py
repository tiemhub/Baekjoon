#dfs와 bfs
#바이러스
import sys

def dfs(v):

    visited[v-1] = 1

    for i in range(n):
        if visited[i] == 0 and line[v-1][i] == 1:
            dfs(i+1)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

visited = [0]*n
line = [[0]*n for i in range(n)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    line[x-1][y-1] = 1
    line[y-1][x-1] = 1

dfs(1)

print(sum(visited)-1)
