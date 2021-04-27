#동적 계획법
#3가지 연산을 이용한 1만들기
#재귀를 이용하지 말고 순차적으로 하는 게 좋을 때도 있다!

import sys

def solve(n):
    if n == 1:
        return 0
    if result[n] != 0:
        print('return',result[n])
        return result[n]
    
    value = solve(n-1) + 1
    if n%3 == 0:
        value = min(value, solve(n//3) + 1)
    elif n%2 == 0:
        value = min(value,solve(n//2) + 1)

           
    result[n] = value
    print(result)
    return value

n = int(sys.stdin.readline().strip())
result = [0]*(n+1)
print(solve(n))
