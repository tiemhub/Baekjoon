#이분탐색
#가장 긴 증가하는 부분 순열
#동적계획법 이용
#10 20 30 70 과 10 20 50 70 수열은 결국 길이가 같다
#이분탐색 실패시 dp 증가, 성공시 값을 바꾼다 => 바꿔도 길이가 변하지는 않는다.
import sys

n = int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().split()))

dp = [-1]*n
flag = 0

for i in li:

    start, end = 0, flag
    
    while start <= end:

        mid = (start + end) // 2
        
        if i > dp[mid]:
            start = mid +1
        elif i < dp[mid]:
            end = mid - 1

    if end >= n:
        flag += 1
    dp[end] = i
    print(dp)

print(len([i for i in dp if (i+1)]))
