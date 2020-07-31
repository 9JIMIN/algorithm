n = int(input())
num = list(map(int, input().split()))
d = [0]*n
res = [[x] for x in num]

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and d[i] < d[j]:
            d[i] = d[j]
            res[i] = res[j] + [num[i]]
    d[i] += 1
ans = max(d)
print(ans)
print(*res[d.index(ans)])