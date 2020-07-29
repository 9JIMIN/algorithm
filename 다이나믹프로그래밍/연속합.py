n = int(input())
num = list(map(int, input().split()))
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = max(d[i-1] + num[i], num[i])

ans = max(d)
print(ans)