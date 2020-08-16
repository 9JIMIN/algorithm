from itertools import product

n, m = map(int, input().split())
p = product(range(1, n+1), repeat=m)

for e in p:
    print(*e)