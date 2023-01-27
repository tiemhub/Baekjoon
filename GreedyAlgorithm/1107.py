"""
1107 리모콘
2023.01.27
Seo Sanghyeok

채널 변경 방법은
채널 입력 -> 채널 UP/DOWN 둘 중 하나

"""
import sys

def solve(n,numbers):
    if n == 100: return 0
    upnum = ''
    downnum = ''
    found = False

    for i in range(len(str(n))):
        if found:
            upnum += numbers[0]
            downnum += numbers[-1]
        elif str(n)[i] in numbers:
            upnum += 'i'
            downnum += 'i'
        else:
            upnum += findNearestNum(i,numbers,True)
            downnum += findNearestNum(i,numbers,True)

        print(upnum,downnum,n)

    return min(int(upnum)-n,n-int(downnum),abs(100-n))    

def findNearestNum(numbers,bool):
    if 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
imnumbers = list(map(int,sys.stdin.readline().split()))
numbers = []
for i in range(10):
    if i not in imnumbers:
        numbers.append(i)

solve(n,numbers)