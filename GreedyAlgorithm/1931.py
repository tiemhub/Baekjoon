#그리디
#최다 회의실 배정
import sys

def findmin(n, end = 0):
    value = 2**31 - 1

    for i in range(n):
        if room[i][0] > end:
            value = min(value, room[i][1])

    print(value)
    return value

    
n = int(sys.stdin.readline().strip())
room = [0]*n

for i in range(n):
    room[i] = list(map(int,sys.stdin.readline().strip().split()))

cnt, end = 0, 0
value = findmin(n)
while True:
    
    if value == 2**31-1:
        break

    cnt += 1
    end = value
    value = findmin(n,end)

print(cnt)
