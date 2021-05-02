#동적 계획법
#LCS 구하기

def search(i,j,n):
    max_value = [j,0]
    for k in cache[i+1:]:

        if j < k[0]:
            temp = k
            if temp[1] > max_value[1]:
                max_value = temp

    return [max_value[0],max_value[1]+1]

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

n = len(str1)
cache = [[0,0] for _ in range(n)] #[인덱스, 길이] 형식으로 저장

for i in range(len(str1)-1,-1,-1):

    for j in range(len(str2)-1,-1,-1):
        if str1[i] == str2[j]:
            cache[i] = search(i,j,n)
            

max_value =  0
for i in range(n):
    max_value = max(max_value,cache[i][1])

print(max_value)

