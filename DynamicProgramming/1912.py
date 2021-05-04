#1912
#연속합
import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().split()))
sum_list = [0]*n
sum_list[0] = num_list[0]

for i in range(n-1):
    sum_list[i+1] = max(sum_list[i]+num_list[i+1],num_list[i+1])

print(max(sum_list))
