#이분 탐색
#k번째 수
import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
li = []

for i in range(1,n+1):
    for j in range(1,n+1):
        li.append(i*j)

li.sort()
print(li[k])
