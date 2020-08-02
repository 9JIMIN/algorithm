n, k = map(int, input().split())

d = [[1]*(n+1) for _ in range(k)]

for i in range(1, k):
    for j in range(1, n+1):
        d[i][j] = (d[i-1][j] + d[i][j-1])%1000000000

print(d[k-1][n])