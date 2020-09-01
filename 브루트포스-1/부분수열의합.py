from itertools import combinations

n, s = map(int, input().split())
num = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    cases = combinations(num, i)
    for sub in cases:
        if sum(sub) == s:
            count += 1

print(count)