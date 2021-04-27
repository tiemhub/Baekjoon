#백트래킹
#n 이하의 숫자 m개로 이루어진 비내림차순 수열(중복 가능)

def solve(dp, n, m, j):
    if dp == m:
        print(' '.join(map(str,out)))
        return
    for i in range(j,n):
        out.append(i+1)
        solve(dp+1,n,m,i)
        out.pop()

n,m = map(int,input().split())
out = []

solve(0, n, m, 0)
