#정렬
#O(n*lgn)으로 풀어보기

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

for _ in range(n):
    print(num_list[_])
