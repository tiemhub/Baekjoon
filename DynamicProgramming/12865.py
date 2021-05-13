#동적계획법
#nap sack
import sys

n, k = map(int,sys.stdin.readline().split())
things = [[0,0] for _ in range(n)]

for i in range(n):
    things[i] = list(map(int,sys.stdin.readline().split()))

value = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    for j in range(k+1):
        if j < things[i][0]:
            value[i][j] = value[i-1][j]
        else:
            value[i][j] = max(things[i][1] + value[i-1][j-things[i][0]],value[i-1][j])

print(value[-1][-1])
