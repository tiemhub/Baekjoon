#백트래킹
#연산자 끼워넣기를 통해 최대값 찾기
global max_val, min_val
max_val = -1000000000
min_val = 1000000000

def caculate(value,dp,operator):
    oper_list[operator] -= 1
    if operator == 0:
        return value + num_list[dp+1]
    elif operator == 1:
        return value - num_list[dp+1]
    elif operator == 2:
        return value * num_list[dp+1]
    elif operator == 3:
        if value > 0:
            return value // num_list[dp+1]
        else:
            return -((-value)//num_list[dp+1])

def solve(dp, n, value):
    global max_val, min_val
    #print(dp,n,value,oper_list)
    if dp == (n-1):
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value
        return
    for i in range(4):
        if oper_list[i] > 0:
            #print(value,dp,i)
            temp = caculate(value,dp,i)
            
            solve(dp+1,n,temp)
            oper_list[i] += 1

n = int(input())
num_list = list(map(int,input().split()))
oper_list = list(map(int,input().split()))

solve(0, n, num_list[0])

print(max_val)
print(min_val)
