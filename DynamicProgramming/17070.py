#동적프로그래밍
#파이프 옮기기1
import sys

value = []

for _ in range(int(sys.stdin.readline().strip())):
    value.append(list(map(int,sys.stdin.readline().split())))
