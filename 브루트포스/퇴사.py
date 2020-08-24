n = int(input())
dp = [0] * (n+10)
for i in range(n):
    t, p = map(int, input().split())
    dp[i+1] = max(dp[i+1], dp[i])
    dp[i+t] = max(dp[i+t], dp[i]+p)
    print(dp)
print(dp[n])