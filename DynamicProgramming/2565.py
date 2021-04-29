#동적계획법
#전깃줄
#도착 지점들이 오름차순을 이루면 겹치지 않는다!

import sys

n = int(sys.stdin.readline().strip())
line = [0]*n

for i in range(n):
    line[i] = list(map(int,sys.stdin.readline().strip().split()))

line.sort()
length = [1]*n

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            length[i] = max(length[i],length[j]+1)


print(n-max(length))
