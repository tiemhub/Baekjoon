#동적 계획법
#LCS 구하기

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()


cache = [[0]*len(str2) for _ in str1] #[인덱스, 길이] 형식으로 저장

for i in range(1,len(str1)):

    for j in range(1,len(str2)):
        if str1[i] == str2[j]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1],cache[i-1][j])


print(cache[-1][-1])
