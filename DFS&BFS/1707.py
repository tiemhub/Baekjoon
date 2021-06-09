#DFS&BFS
#이분 그래프
#시작 점으로부터 깊이에 따라 1,-1,1을 부여, 부여할 값과 현재값이 다르면 이진트리x
import sys
from collections import deque

global done

def bfs(start):
    global done
    
    queue = deque()
    queue.append(start)
    visited[start] = 1
    value = -1

    while queue and not done:

        for _ in range(len(queue)):

            i = queue.popleft()

            for j in line[i]:
                if visited[j] == 0:
                    visited[j] = value
                    queue.append(j)
                elif visited[j] != value:
                    done = True
                    break

        value *= -1

for _ in range(int(sys.stdin.readline().strip())):
    v, e = map(int,sys.stdin.readline().split())

    line = [[] for _ in range(v)]
    visited = [0]*v
    done = False

    for _ in range(e):
        x, y = map(int,sys.stdin.readline().split())
        line[x-1].append(y-1)
        line[y-1].append(x-1)

    for i in range(v):
        if visited[i] == 0:
            bfs(i)

    print("YES" if not done else "NO")
