#정수론
#최대공약수와 최소공배수
import sys

for _ in range(int(sys.stdin.readline().strip())):
    a, b = map(int,sys.stdin.readline().split())
    gcd = 0
    lcm = 0

    for i in range(a,0,-1):
        if a%i == 0 and b%i == 0:
            gcd = i
            break

    lcm = a * b / gcd

    print(gcd)
    print(int(lcm))
