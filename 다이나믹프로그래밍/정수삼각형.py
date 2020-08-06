n = int(input())

a = [int(input())]
for i in range(2, n+1):
    d = list(map(int, input().split()))
    for j in range(i):
        if j == 0: d[j] += a[0]
        elif j == i-1: d[j] += a[i-2]
        else: d[j] += max(a[j-1], a[j])
    a = d

print(max(a))