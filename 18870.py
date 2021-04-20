#정렬
#압축 정렬

n = int(input())
num_list = list(map(int,input().split()))

#중복되지 않는 값으로 배열을 제작 후 정렬
index_list = []
for i in num_list:
    if not i in index_list:
        index_list.append(i)
index_list.sort()

#출력
for i in num_list:
    print(index_list.index(i),end=" ")
