from itertools import combinations_with_replacement

n, m = map(int, input().split())
c = combinations_with_replacement(range(1, n+1), m)

for e in c:
    print(*e)