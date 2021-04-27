#동적 계획법
#집을 칠하는 비용의 최솟값 구하기
#dp 이긴 하지만 dfs로도 풀릴 듯 하다
#dpf로도 해결은 가능하지만, dp의 핵심은 각 경우의 적정값을 저장하는 것이다!!

global min_value
min_value = 1000

def solve(n, dp, value, i = -1):
    global min_value
    
    if dp == n:
        min_value = min(min_value,value)
        return

    if i != 0:
        solve(n, dp+1, value+price_list[dp][0], 0)
    if i != 1:
        solve(n, dp+1, value+price_list[dp][1], 1)
    if i != 2:
        solve(n, dp+1, value+price_list[dp][2], 2)


n = int(input())

price_list = [0]*n

for i in range(n):
    price_list[i] = list(map(int,input().split()))

solve(n, 0, 0)

print(min_value)
    
