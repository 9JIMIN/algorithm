from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

c = combinations_with_replacement(num, m)

for e in c:
    print(*e)

