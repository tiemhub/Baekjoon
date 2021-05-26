#이분탐색
#수 찾기
import sys

def search(i,start,end):
    
    mid = (start+end)//2

    if a[mid] == i:
        return 1
    elif start == end:
        return 0
    elif a[mid] > i:
        return search(i,start,mid-1)
    elif a[mid] < i:
        return search(i,mid+1,end)
    

n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

a.sort()

for i in list(map(int,sys.stdin.readline().split())):
    print(search(i,0,n-1))
