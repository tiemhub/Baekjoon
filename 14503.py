"""

로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 
  1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
  2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
  1. 반시계 방향으로 90도 회전한다.
  2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
  3. 1번으로 돌아간다.
2,3번 통합 가능 => 현재 자리에서 청소되지 않은 빈칸 방향을 return 해주기
"""
import sys

def canmove(r,c,d):
    d = (d-1)%4

    for i in range(4):
        if d==0 and r != 0: #이동방향이 북쪽이고, 제일 위가 아닐때
            if maps[r-1][c] == 0: #북쪽 타일이 청소하지 않았다면
                return d #이동방향은 북쪽
        if d==1 and (c != len(maps[0])-1): #이동방향이 동쪽이고
            if maps[r][c+1] == 0:
                return d
        if d==2 and (r != len(maps)-1):
            if maps[r+1][c] == 0:
                return d
        if d==3 and (c != 0):
            if maps[r][c-1] == 0:
                return d
        d = (d-1)%4
    
    return 5


n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

# 0 => 청소되지 않음, 1 => 벽, 2 => 청소됨
maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
end = False

while not end:
    print(r,c,d,cnt)
    # 청소되어 있지 않으면 청소하기
    if maps[r][c] == 0:
        maps[r][c] = 2
        cnt += 1
    
    direction = canmove(r,c,d)
    print(direction)
    if direction == 0:
        r, c, d = r-1, c, direction
    elif d == 1:
        r, c, d = r, c+1, direction
    elif d == 2:
        r, c, d = r+1, c, direction
    elif d == 3:
        r, c, d = r, c-1, direction
    else: #만약 주변에 빈 칸이 없다면
        if d == 0:
            if (r != (len(maps)-1)) and (maps[r+1][c] != 1):
                r, c = r+1, c
            else:
                end = True
        elif d == 1:
            if (c != 0) and (maps[r][c-1] != 1):
                r, c = r, c-1
            else:
                end = True
        elif d == 2:
            if (r != 0) and (maps[r-1][c] != 1):
                r, c = r-1, c
            else:
                end = True
        elif d == 3:
            if (c != (len(maps[0])-1)) and (maps[r][c+1] != 1):
                r, c = r, c+1
            else:
                end = True

print(cnt)


