#DFS&BFS
#토마토 3차원
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

if n == k:
    print(0)
else:
    times = 0
    end = False
    queue= deque()
    queue.append(n)

    while queue and not end:

        for _ in range(len(queue)):
            i = queue.popleft()

            if i*2 == k:
                end = True
                break
            else:
                queue.append(i*2)

            if i+1 == k:
                end = True
                break
            else:
                queue.append(i+1)

            if i-1 == k:
                end = True
                break
            else:
                queue.append(i-1)

        times += 1

    print(times)

        
