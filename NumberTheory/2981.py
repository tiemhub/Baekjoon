#정수론
#검문
#수학적 지식 필요, a-b,b-c,c-d의 공약수가 이 문제의 답이다.
import sys

def check(i):
    result = True
    value = num_list[0]%i
    for j in num_list[1:]:
        if value != j%i:
            result = False
            break

    return result

n = int(sys.stdin.readline().strip())
num_list = [0]*n

for i in range(n):
    num_list[i] = int(sys.stdin.readline().strip())

for i in range(2,min(num_list)):
    if check(i):
        print(i,end=" ")
