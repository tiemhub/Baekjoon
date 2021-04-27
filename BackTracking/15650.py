#백트래킹
#n 이하의 숫자 m개로 이루어진 오름차순 순열
#16549번에서 그 전에 숫자 몇을 추가했는지 알려주는 요소 j를 추가함을 통해
#탐색 범위를 j에서 n까지로만 제한시킨다.

def solve(dp, n, m, j):
    if dp == m:
        print(' '.join(map(str,out)))
        return
    for i in range(j,n):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(dp+1, n, m, i)
            visited[i] = False
            out.pop()

n,m = map(int,input().split())
visited = [False] * n
out = []

solve(0, n, m, 0)
