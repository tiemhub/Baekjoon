"""
문제
볼록 다각형이 있고, 여기서 3개의 연속된 점을 선택해서 삼각형을 만든다. 그 다음, 만든 삼각형을 다각형에서 제외한다. 원래 다각형이 N개의 점이 있었다면, 이제 N-1개의 점으로 구성된 볼록 다각형이 된다. 위의 과정은 남은 다각형이 삼각형이 될 때까지 반복한다.

볼록 다각형의 점이 시계 방향순으로 주어진다. 마지막에 남은 삼각형은 여러 가지가 있을 수 있다. 이때, 가능한 넓이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 볼록 다각형 점의 수 N (3 ≤ N ≤ 35)이 주어진다. 둘째 줄부터 N개의 줄에는 볼록 다각형을 이루고 있는 점이 시계 방향 순서로 주어진다. 좌표는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

naive- 다각형 내 최대 크기의 삼각형
연속된 점을 선택하여 삼각형 제거가 영향을 미치나 = 다각형 내 최대 크기의 삼각형을 연속된 점으로 구성된 삼각형을 제거하는 것으로 만들 수 있는가
=> 가능해보임
다각형 내 최대 크기의 삼각형 3점을 선택하는 방법은? => brute force
"""

import sys

dots = []

for _ in range(int(sys.stdin.readline().strip())):
    x,y = map(int,sys.stdin.readline().split())
    dots.append([x,y])

max_area = 0

for i in range(len(dots)-2):
    for j in range(i+1, len(dots)-1):
        for k in range(j+1, len(dots)):
            area = abs(dots[i][0]*dots[j][1] + dots[j][0]*dots[k][1] + dots[k][0]*dots[i][1] - dots[j][0]*dots[i][1] - dots[k][0]*dots[j][1] - dots[i][0]*dots[k][1]) * 0.5
            max_area = max(max_area, area)

print(max_area)