#그리디 알고리즘
#주유소
import sys

n = int(sys.stdin.readline().strip())
dis = list(map(int,sys.stdin.readline().strip().split()))
price = list(map(int,sys.stdin.readline().strip().split()))

result = dis[0]*price[0]
flag = price[0]

for i in range(1,n-1):
    if flag > price[i]:
        flag = price[i]
    result += dis[i]*flag

print(result)
