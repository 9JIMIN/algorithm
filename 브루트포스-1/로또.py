from itertools import combinations

while True:
    i, *s = list(map(int, input().split()))
    if i == 0: break

    s = list(combinations(s, 6))
    for c in s:
        print(*c)
    print()