# import sys
# M = int(sys.stdin.readline())
# N = M // 2
# stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# row = [sum(i) for i in stat]
# col = [sum(i) for i in zip(*stat)]
# newstat = [i+ j for i, j in zip(row, col)]
# allstat = sum(newstat) // 2
# newstat.sort()

# def main(addup, i):
#     if addup >= 0:
#         return -addup
#     if i == -1:
#         return addup
#     x = main(addup + newstat[i], i-1)
#     if x == 0:
#         return 0
#     return max(x, main(addup, i-1))

# print(-main(-allstat, M - 2))

from itertools import combinations

def subsets(n):
    for i in range(1, n): yield from combinations(range(n), i)

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
res = float('inf') # 양의 무한대 float('-inf') 이건 음의 무한대

for sub in subsets(n):
    rest = set(range(n)) - set(sub)
    cur = 0
    for i in sub:
        for j in sub: cur+= s[i][j]
    for i in rest:
        for j in rest: cur-= s[i][j]
    res = min(res, abs(cur))
print(res)