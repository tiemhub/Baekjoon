#동적계획법
#계단오르기 최댓값 구하기

n = int(input())
score_list = []

for _ in range(n):
    score_list.append(int(input()))

#최댓값은 전전계단의 최댓값+현재 계단값 or 전전전계단의 최댓값+전계단의 값+현재 계단값
#그러나 이 규칙은 계단이 최소 3개 이상이여야 하므로 예외를 처리 해준다.
if n <= 2:
    print(sum(score_list))
else:
    sum_list = [0,score_list[0],score_list[0]+score_list[1]]

    for i in range(3,n+1):
        value = max(sum_list[i-2],score_list[i-2]+sum_list[i-3]) + score_list[i-1]
        sum_list.append(value)

    print(sum_list[-1])
