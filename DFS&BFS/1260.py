#dfs와 bfs
#dfs와 bfs 기초
import sys

def dfs(v):

    print(v,end =' ')
    visited[v-1] = 1

    for i in range(n):
        if visited[i] == 0 and line[v-1][i] == 1:
            dfs(i+1)

def bfs(v):

    queue = [v]
    visited[v-1] = 0

    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(n):
            if visited[i] == 1 and line[v-1][i] == 1:
                queue.append(i+1)
                visited[i] = 0

    
n, m, v = map(int,sys.stdin.readline().split())

visited = [0]*n
line = [[0]*n for i in range(n)]

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    line[x-1][y-1] = 1
    line[y-1][x-1] = 1

dfs(v)
print()
bfs(v)
