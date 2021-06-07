#DFS&BFS
#숨바꼭질
#조금 더 안정적인 알고리즘 필요, 순회에 일정 조건이 필요
import sys
from collections import deque

visited = [False]*100001
n,k = map(int,sys.stdin.readline().split())

times = -1
end = False
queue= deque()
queue.append(n)

while queue and not end:

    for _ in range(len(queue)):
        i = queue.popleft()

        if i == k:
            end = True
            break

        for j in [i+1,i-1,i*2]:
            if 0 <= j < 100001:
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)
                    

    times += 1

print(times)

        
