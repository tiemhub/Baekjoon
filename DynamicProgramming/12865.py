#동적계획법
#nap sack
import sys

n, k = map(int,sys.stdin.readline().split())
things = [[0,0] for _ in range(n)]

for i in range(n):
    things[i] = list(map(int,sys.stdin.readline.split()))
