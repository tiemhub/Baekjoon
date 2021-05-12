#동적 프로그래밍
#1,2,3 더하기
import sys

def solve(n):
    if cache[n] != 0:
        return cache[n]
    
    cache[n] = solve(n-1) + solve(n-2) + solve(n-3)
    return cache[n]

cache = [0,1,2,4,7,13] + [0]*5
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    print(solve(n))

