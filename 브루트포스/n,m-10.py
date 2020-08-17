from itertools import product

n, m = map(int, input().split())
num = sorted(set(map(int, input().split())))

p = list(product(num, repeat=m))

for e in p:
    print(*e)