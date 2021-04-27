#정렬
#O(n^2)으로 풀어보기

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        if num_list[i]>num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

for _ in range(n):
    print(num_list[_])
