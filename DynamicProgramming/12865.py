#동적계획법
#nap sack
import sys

n, k = map(int,sys.stdin.readline().split())
things = [[0,0] for _ in range(n)]

for i in range(n):
    things[i] = list(map(int,sys.stdin.readline().split()))

things.sort(reverse = True, key = lambda x : (x[1],x[0]))
cache = []
isin = False
for i in things:
    for j in cache:
        if i[0] + j[0] <= k:
            cache.append([i[0]+j[0],i[1]+j[1]])
            isin = True
    if not isin:
        cache.append(i)
        

print(max(cache,key = lambda x : x[1])[1])
