#동적계획법
#포도주 최대로 마시기
import sys

n = int(sys.stdin.readline().strip())

wine = [0]*n

for i in range(n):
    wine[i] = int(sys.stdin.readline().strip())

a,b,c = 0, 0, 0
s1, s2 = 0, 0

for i in range(n):
    s1, s2 = s2, wine[i]
    value = max(a+s1+s2,b+s2,c)
    a,b,c = b,c,value

print(max(a,b,c))
