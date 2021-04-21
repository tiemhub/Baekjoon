#백트래킹
#n 이하의 숫자 m개로 이루어진 수열(중복 가능)

def solve(dp, n, m):
    if dp == m:
        print(' '.join(map(str,out)))
        return
    for i in range(n):
        out.append(i+1)
        solve(dp+1,n,m)
        out.pop()

n, m = map(int,input().split())
out = []

solve(0,n,m)
