#DFS&BFS
#숨바꼭질
#조금 더 안정적인 알고리즘 필요, 순회에 일정 조건이 필요
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

        
