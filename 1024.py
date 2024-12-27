"""
문제
N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 L이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

길이가 N이면서 연속된 정수 리스트의 조건 = sum(N)을 뺐을 때, N으로 나누어 떨어짐


"""

import sys

n,l = map(int,sys.stdin.readline().split())

for L in range(l, 101):
    sum_L = L * (L-1) / 2
    if (n - sum_L) % L:
        continue
    else:
        start = int((n - sum_L) // L)
        print(start)
        if start < 0:
            continue
        ans = [x for x in range(start, start+L)]
        break
else:
    ans = [-1]

print(*ans)


