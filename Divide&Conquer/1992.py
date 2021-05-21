#분할정복
#쿼드트리
import sys

def solve(x, y, n):
    if possible(x,y):
        return str(data[x[0]][y[0]])
    else:
        string = '('
        string += solve(x[:n//2],y[:n//2],n//2)
        string += solve(x[:n//2],y[n//2:],n//2)
        string += solve(x[n//2:],y[:n//2],n//2)
        string += solve(x[n//2:],y[n//2:],n//2)
        string += ')'
        return string
    
def possible(x,y):
    value = data[x[0]][y[0]]

    for i in x:
        for j in y:
            if value != data[i][j]:
                return False
    return True

n = int(sys.stdin.readline().strip())
data = []

for _ in range(n):
    data.append(sys.stdin.readline().strip())

print(solve([i for i in range(n)],[i for i in range(n)],n))
