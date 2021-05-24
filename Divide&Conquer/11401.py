#분할정복
#(페르마의 소정리를 이용한) 이항 계수
#페르마의 소정리가 
import sys

def solve(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    if n == k:
        return 1
    elif n == k+1:
        return n
    return solve(n-1,k-1)+solve(n-1,k)

n, k = map(int,sys.stdin.readline().split())

print(solve(n,k))
