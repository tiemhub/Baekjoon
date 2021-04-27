#정렬
#2차원 배열의 1번째 요소부터 정렬

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(list(map(int,input().split())))

num_list.sort(key = lambda x : (x[1],x[0]))

for i in range(n):
    print(num_list[i][0],num_list[i][1])
    
