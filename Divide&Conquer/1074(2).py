#Z
#수학적 조건을 이용한 선택적 배제를 통한 재귀

#카운팅 방법 -> 위치 확인 후 앞 부분은 셌다고 판정
#위치 확인 방법 -> 위치를 계속 리스케일링?
import sys

def solve(n,r,c):
    size = 2**(n-1)
    if n==0:
        return 0
    
    if r < size:
        if c < size:
            return solve(n-1,r,c)
        else:
            cnt = ((size)**2)
            return cnt + solve(n-1,r,c-(size))
    else:
        if c < size:
            cnt = ((size)**2)*2
            return cnt + solve(n-1,r-(size),c)
        else:
            cnt = ((size)**2)*3
            return cnt + solve(n-1,r-(size),c-(size))

n, r, c = map(int,sys.stdin.readline().split())

print(solve(n,r,c))