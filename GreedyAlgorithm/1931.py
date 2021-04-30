#그리디
#최다 회의실 배정
import sys

    
n = int(sys.stdin.readline().strip())
room = [0]*n

for i in range(n):
    room[i] = list(map(int,sys.stdin.readline().strip().split()))

room.sort(key = lambda x : (x[1],x[0]))

end, cnt = 0, 0

for i in range(n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)
