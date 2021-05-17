#동적프로그래밍
#파이프 옮기기1
import sys

n = int(sys.stdin.readline().strip())
value = []
dp = [[0]*n for _ in range(n)]

for _ in range(int(sys.stdin.readline().strip())):
    value.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if not 
