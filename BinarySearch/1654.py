#이분탐색
#랜선 자르기
import sys

k, n = map(int,sys.stdin.readline().split())
value = [0]*k

for i in range(k):
    value[i] = int(sys.stdin.readline().strip())

start,end = 1, max(value)

while not start > end:
    cnt = 0
    mid = (start + end)//2
    for i in value:
        cnt += (i//mid)

    if cnt >= n:
        start, end = mid+1, end
    elif cnt < n:
        start, end = start, mid -1

print(end)
