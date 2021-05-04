#1912
#연속합
import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().split()))

result = num_list[0]
a,b,c = 0, 0, 0 #총합, 양수

for i in num_list:
    if i >= 0:
        if b == 0:
            a += i
        else:
            c += i
    else:
        if c == 0:
            b += i
        else:
            result = max(result,a,c,a+b+c)
            a = max(c,a+b+c)
            c = 0
            b = i
    print(a,b,c,result)

if a==0:
    print(result)
else:
    print(max(result,a,c,a+b+c))
