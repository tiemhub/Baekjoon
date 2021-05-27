#이분탐색
#숫자카드
import sys

def search(i,start,end):
    
    mid = (start+end)//2

    if a[mid] == i:
        return a[start:end+1].count(i)
    elif start >= end:
        return 0
    elif a[mid] > i:
        return search(i,start,mid-1)
    elif a[mid] < i:
        return search(i,mid+1,end)
    
n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline().strip())
b = list(map(int,sys.stdin.readline().split()))

for i in b:
    print(search(i,0,n-1),end=' ')
