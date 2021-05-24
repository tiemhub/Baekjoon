#분할정복
#행렬의 곱셈
import sys

n, m = map(int,sys.stdin.readline().split())
a = [[0]*n for i in range(n)]

for i in range(n):
    a[i] = list(map(int,sys.stdin.readline().split()))

m, k = map(int,sys.stdin.readline().split())
b = [[0]*k for i in range(m)]

for i in range(m):
    b[i] = list(map(int,sys.stdin.readline().split()))

result = [[0]*k for i in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += (a[i][l]*b[l][j])

for i in range(n):
    for j in range(k):
        print(result[i][j],end=" ")
    print()
