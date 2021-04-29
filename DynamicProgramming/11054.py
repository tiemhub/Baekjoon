#동적계획법
#가장 긴 바이토닉  수열
import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().strip().split()))
low = [1]*n
high = [1]*n

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            high[i] = max(high[i],high[j]+1)
    print(high)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if num_list[i] > num_list[j]:
            low[i] = max(low[i],low[j]+1)
    print(low)

max_len = 0

for i in range(n):
    max_len = max(max_len,low[i]+high[i]-1)

print(max_len)
