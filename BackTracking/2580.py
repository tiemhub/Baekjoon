#백트래킹
#스도쿠
import sys

end = False

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

def solve(dp,n):
    global end
    if dp == n:
        print_sudoku()
        end = True
        return
    x,y = zero_ind[dp]
    for i in is_promising(x,y):
        sudoku[x][y] = i
        solve(dp+1,n)
        if end:
            break
        sudoku[x][y] = 0
        
    

def print_sudoku():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=" ")
        print()
                

sudoku = []

for _ in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().split())))

zero_ind = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_ind.append([i,j])
            
solve(0,len(zero_ind))
