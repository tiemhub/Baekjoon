#정수론
#배수와 약수
import sys

while True:
    a,b = map(int,sys.stdin.readline().split())

    if (a,b) == (0,0):
        break

    if not a%b:
        print('multiple')
    elif not b%a:
        print('factor')
    else:
        print('neither')
