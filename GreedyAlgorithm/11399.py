#그리디 알고리즘
#ATM

import sys

n = int(sys.stdin.readline().strip())
wating = list(map(int,sys.stdin.readline().strip().split()))

wating.sort()
sum_val = 0

for i in range(n):
    sum_val += wating[i] * (n-i)

print(sum_val)
