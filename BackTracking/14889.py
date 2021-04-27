#백트래킹
#스타트와 링크

global min_gap
min_gap = 100

def solve(dp,m,n):
    global min_gap
    
    if dp == m:
        min_gap = calculate(m, min_gap)

    for i in range(n,m*2):
        if not visited[i]:
            visited[i] = True
            solve(dp+1,m,i)
            visited[i] = False

def calculate(m,value):
    gap = 0

    for i in range(2*m):
        for j in range(2*m):
            if visited[i] and visited[j]:
                gap += status[i][j]
            elif not visited[i] and not visited[j]:
                gap -= status[i][j]

    return min(abs(gap), min_gap)
        
n = int(input())
status = []

for _ in range(n):
    status.append(list(map(int,input().split())))

visited = [False]*n

solve(0 ,n // 2, 0)

print(min_gap)
