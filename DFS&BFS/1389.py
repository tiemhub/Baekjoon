"""
케빈 베이컨의 6단계 법칙

플로이드워셜 알고리즘
각 노드간 최단 거리를 구하는 O(n^3)
"""
import sys

n,m = map(int,sys.stdin.readline().split())

relation = [[999]*n for i in range(n)]

for k in range(m):
    i,j = map(int,sys.stdin.readline().split())
    relation[i-1][j-1] = 1
    relation[j-1][i-1] = 1

for i in range(n):
    for j in range(n):
        relation[j][j] = 0
        for k in range(j+1,n):
            relation[j][k] = min(relation[j][k],relation[j][i]+relation[i][k])
            relation[k][j] = relation[j][k]

flag, val = 0, 999
for i in range(n):
    if val > sum(relation[i]):
        flag, val = i, sum(relation[i])

print(flag+1)