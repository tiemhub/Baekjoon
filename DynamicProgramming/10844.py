#동적계획법
#계단수 찾기
import sys
    
n = int(sys.stdin.readline().strip())

stnum = [[0]*10 for _ in range(n)]

for i in range(n):
    for j in range(10):
        if i == 0 and j != 0:
            stnum[i][j] = 1

        elif j == 0:
            stnum[i][j] = stnum[i-1][j+1]
        elif j == 9:
            stnum[i][j] = stnum[i-1][j-1]
        else:
            stnum[i][j] = stnum[i-1][j+1] + stnum[i-1][j-1]


print(sum(stnum[n-1])%1000000000)
