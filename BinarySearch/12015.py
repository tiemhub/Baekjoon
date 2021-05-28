#이분탐색
#가장 긴 증가하는 부분 순열
import sys

n = int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().split()))

start, end = 1, n-1

while start <= end:

    
    mid = (start + end) // 2

    
