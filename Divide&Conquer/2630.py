#분할정복
#색종이 만들기
import sys

def solve(x,y,n):
    global blue, white

    if possible(x,y):
        if paper[x[0]][y[0]]:
            blue +=1
        else:
            white +=1
    else:
        solve(x[n//2:],y[n//2:],n//2)
        solve(x[n//2:],y[:n//2],n//2)
        solve(x[:n//2],y[n//2:],n//2)
        solve(x[:n//2],y[:n//2],n//2)
    
            

def possible(x,y):
    value = paper[x[0]][y[0]]

    for i in x:
        for j in y:
            if value != paper[i][j]:
                return False
    return True
            
global blue, white
blue, white = 0, 0
n = int(sys.stdin.readline().strip())
paper = []

for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

solve([i for i in range(n)],[i for i in range(n)],n)

print(white,blue,sep="\n")
