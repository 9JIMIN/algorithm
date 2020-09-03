# import sys
# sys.setrecursionlimit(10000) # 재귀제한 10000으로 변경.

# def dfs(v):
#     visited[v] = True
#     for e in rel[v]:
#         if not visited[e]:
#             dfs(e)

# n, m = map(int, input().split())
# rel = [[] for _ in range(n + 1)]
# visited = [False for _ in range(n+1)]
# count = 0

# for _ in range(m):
#     u, v = map(int, input().split())
#     rel[u].append(v)
#     rel[v].append(u)
    
# for i in range(1, n + 1):
#     if not visited[i]:
#         dfs(i)
#         count += 1

# print(count)

import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for e in rel[x]:
        if not visited[e]:
            print(e)
            dfs(e)

n, m = map(int, input().split())
rel = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    rel[u].append(v)
    rel[v].append(u)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)