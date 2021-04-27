#동적 계획법
#00이 포함된 길이 n의 이진수열 => 피보나치 수열??
#파이썬에서 배열을 append할 경우, 동적할당이 일어나서
#계산시간이 늘어나거나 재귀오류가 난다.
#그러므로, 미리 공간을 할당하고 값을 바꿔주는 편이 빠르다.

def solve(n):
    if n < len(cache):
        return cache[n]
    value = (solve(n-2)+solve(n-1))%15746
    cache.append(value)
    print(cache)
    return value
    

cache = [0,1,2]

n = int(input())

print(solve(n))
