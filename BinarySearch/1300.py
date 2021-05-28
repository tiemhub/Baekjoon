#이분 탐색
#k번째 수
import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
li = []

start, end = 1, k

while start <= end:
    
    cnt = 0
    mid = (start + end) // 2

    for i in range(1,n+1):
        cnt += min(n,mid//i)

    if cnt >= k:
        result = mid #start,mid,end값은 계속 바뀌므로 값을 저장
        end = mid - 1
    else:
        start = mid + 1

print(result)
