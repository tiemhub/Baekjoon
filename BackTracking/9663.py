#백트래킹
#n-queen
#nxn의 체스판 위에 올라가는 퀸의 개수

#dfs 알고리즘은 완성되어 있으나, 판정 알고리즘의 한계로 인해
#완벽한 판정이 불가능함.
#dfs 알고리즘을 완벽히 했다는 것에 의의
#저장방식 변경을 통해 해결 가능!

global cnt
cnt = 0

def solve(dp, n, i):
    """dp = 깊이, n=탐색 범위, i = 이전 뎁스의 위치"""
    global cnt
    if dp == n:
        cnt += 1
        return
    for j in range(i,n*n):
        if possible(j,n):
            print(location,j)
            location.append(j)
            solve(dp+1,n,j)
            location.pop()

def possible(i,n):
   
    for dot in location:
        if i//n == dot//n:
            return False
        elif i%(n+1) == dot%(n+1):
            return False
        elif i%(n-1) == dot%(n-1):
            return False
        elif i%n == dot%n:
            return False

    return True
        

n = int(input())
location = []

solve(0,n,0)

print(cnt)
