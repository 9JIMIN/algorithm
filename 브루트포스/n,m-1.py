# from itertools import permutations

# n, m = map(int, input().split())

# d = list(permutations([i for i in range(1, n+1)], m))

# for i in range(len(list(d))):
#     for j in range(m):
#         print(d[i][j], end=' ')
#     print('', end='\n')

from itertools import permutations

n, m = map(int, input().split())
p = permutations(range(1, n+1), m)

for e in p:
    print(*e)