#그리디 알고리즘
#동전
import sys

n, money = map(int,sys.stdin.readline().split())
values = [0]*n
result = 0

for i in range(n):
    values[i] = int(sys.stdin.readline().strip())

values.reverse()

for i in values:
    result += money//i
    money %= i

print(result)
