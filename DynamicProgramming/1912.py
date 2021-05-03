#1912
#연속합
import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().split()))

result = num_list[0]
s1, s2 = num_list[0], num_list[0]

for i in num_list[1:]:
    s2 += i
    if i < 0:
        if s2 < 0:
            result = max(s1,result)
            s1, s2 = 0, 0
    else:
        s1 += i
    print(s1,s2,result)

print(max(result,s1))
