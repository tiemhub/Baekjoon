#동적 계획법
#삼각형 에서의 최소의 걸

n = int(input())
dis_list = []

for _ in range(n):
    dis_list.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    for j in range(len(dis_list[i])):
        dis_list[i][j] = max(dis_list[i+1][j],dis_list[i+1][j+1]) + dis_list[i][j]

print(dis_list[0][0])
