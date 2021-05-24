#분할정복
#곱셈
import sys

def solve(a,b,c):
    if b == 0:
        return 1%c
    elif b == 1:
        return a%c
    
    if b%2:
        return (solve(a,b//2,c)**2)*a%c
    else:
        return solve(a,b//2,c)**2%c
    
a,b,c = map(int,sys.stdin.readline().split())

print(solve(a,b,c))
