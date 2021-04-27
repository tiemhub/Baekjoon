#백트래킹
#n 이하의 숫자, m개의 순열

def solve(dp, n, m):
    if dp == m: #깊이가 m과 같다면 출력
        print(' '.join(map(str,out)))
        return
    for i in range(n): #i까지의 수에 대해 탐색
        if not visited[i]: #탐색하지 않았다면
            visited[i] = True #탐색 완료 처리
            out.append(i+1) #출력에 추가
            solve(dp+1, n, m) #깊이 증가 후 탐색
            visited[i] = False #탐색 초기화
            out.pop() #최후방 요소 제거

n,m = map(int,input().split())
visited = [False] * n
out = []

solve(0, n, m)


"""
visited를 초기화 하지 않는 이유

visited는 out에 들어있는 요소를 나타내므로, visited를 초기화하지 않을 경우,
프로그램이 특정 요소를 들어가있는 상태로 간주하여 모든 경우에 대한 탐색이 불가능함.

out.pop을 사용하는 이유

out은 출력용 배열로, 최후방 요소는 가장 깊은 깊이를 가지고 있다.
그렇기에 깊이 탐색이 끝나면 옆 가지에 대한 깊이 탐색을 펼치므로,
최후방의 요소는 지워지고 옆 가지에서 새로 채워나가야한다.
그러므로 최후방의 요소가 제거되어야 다음 가지에서 정상적인 탐색을 펼칠 수 있다.
"""
