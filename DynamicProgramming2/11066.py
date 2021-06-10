#동적 프로그래밍 2
#파일 합치기
#그리디 알고리즘이 아니라 특정 조건이 필
import sys

def solve(li):

    if len(li) == 2:
        return sum(li)

    li2 = [0]*(len(li)-1)
    floor = 10000
    flag = 0

    for i in range(len(li2)):
        li2[i] = li[i] + li[i+1]
        if li2[i] < floor:
            floor = li2[i]
            flag = i
    print(li)        
    print(li2)
    print(li[:flag]+[li2[flag]]+li[flag+2:])
    print(floor)
    print()
    
    return floor + solve(li[:flag]+[li2[flag]]+li[flag+2:])

    

    

for _ in range(int(sys.stdin.readline().strip())):

    k = int(sys.stdin.readline().strip())
    value = list(map(int,sys.stdin.readline().split()))

    print(solve(value))
    
