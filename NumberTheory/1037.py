#정수론
#약수의 성질
import sys

n = int(sys.stdin.readline().strip())
aliqout = list(map(int,sys.stdin.readline().split()))
    

print(max(aliqout)*min(aliqout))
