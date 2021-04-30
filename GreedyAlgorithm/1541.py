#그리디
#괄호로 최솟값만들기
import sys

formula = str(sys.stdin.readline().strip())
minus = False
sum_val = 0
num = 0

for i in formula:
    if not minus:
        if i == '+':
            sum_val += num
            num = 0
        elif i == '-':
            sum_val += num
            num = 0
            minus = True
        else:
            num = num*10 + int(i)
    else:
        if i == '+' or i == '-':
            sum_val -= num
            num = 0
        
        else:
            num = num*10 + int(i)

if not minus:
    sum_val += num
else:
    sum_val -= num

print(sum_val)
