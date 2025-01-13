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

def checkclean(r,c):
    check = True

    if (r != 0):
        if maps[r-1][c] == 0:


n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

# 0 => 청소되지 않음, 1 => 벽, 2 => 청소됨
maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

cnt = 0

while True:

    # 청소되어 있지 않으면 청소하기
    if maps[r][c] == 0:
        maps[r][c] = 2
        cnt += 1
    
    if checkclean(r,c):
