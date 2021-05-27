#이분탐색
#공유기 설치
import sys

n,c = map(int,sys.stdin.readline().split())
home = [0]*n


for i in range(n):
    home[i] = int(sys.stdin.readline().strip())
    
home.sort()
start, end = 1,home[n-1]-home[0]

while start <= end:

    cnt,flag = 1, home[0]
    mid = (start + end) // 2
    
    for i in home:
        if i - flag >= mid:
            cnt += 1
            flag = i
            
    if cnt >= c:
        start = mid+1
    else:
        end = mid-1

print(end)
