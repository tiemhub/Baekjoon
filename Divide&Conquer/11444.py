#분할정복
#분할정복을 이용한 피보나치 수열
import sys

def multiply(arr1,arr2,n):
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (arr1[i][k]%1000000007*arr2[k][j]%1000000007)
            result[i][j] %= 1000000007
    return result

def solve(a,b,n):
    if b == 1 or b == 0:
        return a
    elif b == -1:
        return [[0]*2 for i in range(2)]

    temp = solve(a,b//2,n)
    
    if b%2:
        return multiply(multiply(temp,temp,n),a,n)
    else:
        return multiply(temp,temp,n)


n = int(sys.stdin.readline().strip())
base = [[1,1],[1,0]]

print(solve(base,n-1,2)[0][0]%1000000007)
