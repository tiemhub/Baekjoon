#Brutal Force
#'666'이 들어가는 n번째 숫자 찾기

n = int(input())
cnt = 0
target = 0

while cnt != n:
    target +=1
    
    if '666' in str(target):
        cnt += 1

print(target)

