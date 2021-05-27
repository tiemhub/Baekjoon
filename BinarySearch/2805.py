#이분탐색
#나무 자르기
import sys

n, m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    
    mid = (start + end) // 2
    cnt = sum([i-mid for i in trees if i>mid])

    if cnt >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
