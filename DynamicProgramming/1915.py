#동적프로그래밍
#가장 큰 정사각형
#1인 좌표를 저장하고 가로세로거리차가 같을 때 맥스값 갱신?
import sys

n,m = map(int,sys.stdin.readline().split())

value = []

for _ in range(n):
    value.append(list(map(int,list(sys.stdin.readline().strip()))))
