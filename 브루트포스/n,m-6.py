from itertools import combinations

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

c = combinations(num, m)

for e in c:
    print(*e)