from itertools import product

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

p = product(num, repeat=m)

for e in p:
    print(*e)
