n, m, v = map(int, input().split())
rel = [[] for _ in range(n+1)] # 노드를 1,2,3.. 이렇게 하기 때문에 0번은 비워줌.
visited = []

for _ in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

def bfs(x):
    visited.append(x)
    for a in visited:
        for b in sorted(rel[a]):
            if b not in visited:
                visited.append(b)
    return visited

def dfs(x):
    visited.append(x)
    for a in sorted(rel[x]):
        if a not in visited:
            dfs(a)
    return visited

print(*dfs(v))
visited = []
print(*bfs(v))