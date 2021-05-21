#분할정복
#종이의 개수
import sys

def solve(x, y, n):
    if possible(x,y):
        result[data[x[0]][y[0]]+1] += 1
    else:
        solve(x[:n//3],y[:n//3],n//3)
        solve(x[:n//3],y[n//3:n//3*2],n//3)
        solve(x[:n//3],y[n//3*2:],n//3)
        solve(x[n//3:n//3*2],y[:n//3],n//3)
        solve(x[n//3:n//3*2],y[n//3:n//3*2],n//3)
        solve(x[n//3:n//3*2],y[n//3*2:],n//3)
        solve(x[n//3*2:],y[:n//3],n//3)
        solve(x[n//3*2:],y[n//3:n//3*2],n//3)
        solve(x[n//3*2:],y[n//3*2:],n//3)
        
    
def possible(x,y):
    value = data[x[0]][y[0]]

    for i in x:
        for j in y:
            if value != data[i][j]:
                return False
    return True

n = int(sys.stdin.readline().strip())
data = []
result = [0,0,0]

for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

solve([i for i in range(n)],[i for i in range(n)],n)

for i in result:
    print(i)
