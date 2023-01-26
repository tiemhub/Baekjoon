#2^n 배열을 z순서로 탐색
#분할정복&재귀
#행과 열에 대한 정보를 어떻게 저장할 것인가
#재귀 n//2 -> n이 1이면 종료
#재귀를 중간에 멈출 수 있는가
#end 변수를 이용해 계속 비교하는 편의 효율과 전부 탐색후 결과만 꺼내오는 것이 빠른가
import sys


def solve(x1,x2,y1,y2,target):
    global cnt, end
    if (x1 == x2):
        cnt += 1
        if (target == (x1,y1)): end = True
        return
    xmid, ymid = (x1+x2)//2, (y1+y2)//2
    if not end:
        solve(x1,xmid,y1,ymid,target)
    if not end:
        solve(xmid+1,x2,y1,ymid,target)
    if not end:
        solve(x1,xmid,ymid+1,y2,target)
    if not end:
        solve(xmid+1,x2,ymid+1,y2,target)


n, r, c = map(int,sys.stdin.readline().split())
cnt = -1 #몇번째인지 세 줄 변수
target = (c,r) #변수의 가시성과 재귀함수에 사용할 변수량을 줄이기 위해 가공
x1, x2 = 0,pow(2,n)-1
y1, y2 = 0,pow(2,n)-1
end = False

solve(x1,x2,y1,y2,target)

print(cnt)