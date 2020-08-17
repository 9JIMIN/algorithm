from itertools import permutations

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

p = permutations(num, m)

for e in p:
    print(*e)