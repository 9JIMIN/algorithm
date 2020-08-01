# N, K = map(int, input().split())

# def f(n, k):
#     if k == 1: return 1
#     if k == 2: return n+1
#     return sum([i*f(n+1-i, k-2) for i in range(1, n+2)])%1000000000

# print(f(N, K))

n, k = map(int, input().split())
mod = 1000000000
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp[i][j] %= mod
print(dp[k][n])