#동적계획법
#가장 긴 증가하는 부분 수열
import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().strip().split()))
length = [1]*n

for i in range(n):

    for j in range(i):
        if num_list[i] > num_list[j]:
            length[i] = max(length[i],length[j]+1)

print(max(length))
