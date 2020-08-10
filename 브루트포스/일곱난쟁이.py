from itertools import combinations

n = [int(input()) for _ in range(9)]
com = combinations(n, 7)

for c in com:
    if sum(c) == 100:
        ans = sorted(c)
        print(*ans, sep='\n')
        break