n = int(input())
dp = [0] * (n+100)
for i in range(1, n+1):
    t, p = tuple(map(int, input().split(' ')))
    dp[i+1] = max(dp[i+1], dp[i])
    dp[i+t] = max(dp[i+t], dp[i]+p)
print(dp[n+1])