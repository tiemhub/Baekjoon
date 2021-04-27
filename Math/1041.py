#Math
#주사위
import sys


def solve(n):
    min1 = dice[0]
    min2 = dice[1]
    min3 = dice[2]

    value = min1 * (5*n**2 - 8*n +4)
    value += min2 * (8*n - 8)
    value += min3 * 4

    return value
    

    
n = int(sys.stdin.readline().strip())
raw_dice = list(map(int,sys.stdin.readline().strip().split()))
dice = []
for i in range(3):
    dice.append(min([raw_dice[i],raw_dice[5-i]]))
dice.sort()
if n == 1:
    print(sum(raw_dice)-max(raw_dice))
else:
    print(solve(n))


