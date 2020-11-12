n, m = map(int, input().split())
rel = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

def dfs(count, node):
    visited[node] = True
    if count == 4:
        print(1)
        exit()
    for x in rel[node]:
        if not visited[x]:
            dfs(count+1, x)
            visited[x] = False

for i in range(n):
    dfs(0, i)
    visited[i] = False
print(0)