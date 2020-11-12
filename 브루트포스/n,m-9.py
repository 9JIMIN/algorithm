# from itertools import permutations

# n, m = map(int,input().split())

# p = sorted(list(map(int, input().split())))
# pset = sorted(set(permutations(p, m)))
# for i in range(len(pset)):
#     flag = 0 
#     if all(pset[i][j] <= pset[i][j+1] for j in range(m-1)):
#         flag = 1
#     if flag: print(*pset[i])

from itertools import combinations

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

c = sorted(list(set(list(combinations(num, m)))))

for e in c:
    print(*e)