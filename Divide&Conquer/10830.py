#분할정복
#행렬 제곱
import sys

def multiply(arr1,arr2,n):
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (arr1[i][k]*arr2[k][j])
            result[i][j] %= 1000
    return result

def solve(a,b,n):
    if b == 1:
        return a

    temp = solve(a,b//2,n)
    
    if b%2:
        return multiply(multiply(temp,temp,n),a,n)
    else:
        return multiply(temp,temp,n)

    

n, b = map(int,sys.stdin.readline().split())
a = [[0]*n for i in range(n)]

for i in range(n):
    a[i] = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    for j in range(n):
        a[i][j] %= 1000
        
result = solve(a,b,n)

for i in range(n):
    for j in range(n):
        print(result[i][j],end=" ")
    print()
