# 체스판 다시 칠하기
# B, W enum을 구성
# 좌상단의 색을 임의로 지정
# 지정된 색깔과 좌표의 특성(n+m/2)를 통해 색을 판별
# 나온 수와 (n*m-숫자) 둘 중 작은 수를 리턴
# 8x8 크기에서만 탐색 -> 답을 보관하는 배열 생성
import sys

def search(n,m,board):
    COLOR = 'B' #임의의 기준색 지정
    cnt = 0 #임의의 색 지정과 맞지 않는 타일의 수를 세는 변수
    for i in range(n,n+8):
        for j in range(m,m+8):
            if ((i+j)%2):
                if (board[i][j] == COLOR): cnt += 1
            else:
                if (board[i][j] != COLOR): cnt += 1

    return cnt

def solve(n,m,board):
    ans = n*m
    for i in range(n-7):
        for j in range(m-7):
            temp = search(i,j,board)
            ans = min(ans,temp,64-temp)
    
    return ans
                

n, m = map(int,sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(input())

print(solve(n,m,board))
