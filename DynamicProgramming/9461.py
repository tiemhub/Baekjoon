#동적 계획법
#파도반 수열

dp = [0,1,1,1,2,2,3,4,5,7,9]
dp += [0] * 90

for _ in range(int(input())):
    n = int(input())
    for i in range(10,n+1):
        dp[i] = (dp[i-1] + dp[i-5])
    print(dp[n])
