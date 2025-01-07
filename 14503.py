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

"""
import sys

n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

visited = [[False] * m] * n
maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

ans = 0

while True:

    if maps[r][c]