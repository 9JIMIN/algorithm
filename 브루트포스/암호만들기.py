from itertools import combinations

L, S = map(int, input().split())
c = sorted(input().split())

for e in combinations(c, L):
    vowel, consonant = 0, 0
    for a in e:
        if a in 'aeiou': vowel += 1
        else: consonant += 1
    if vowel >= 1 and consonant >= 2:
        print(''.join(e))