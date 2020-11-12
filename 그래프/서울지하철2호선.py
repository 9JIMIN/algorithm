import sys
from collections import deque
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n = int(input())
link = [[] for i in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

circuit = [0]*(n+1)
visitStack = []
findCircuit = False
def dfs(i):
    # 순환선을 기록.
    global findCircuit

    visitStack.append(i)
    for x in link[i]:
        if x in visitStack and len(visitStack)-visitStack.index(x)>=3:
            findCircuit = True
            for v in visitStack[:x]:
                circuit[v] = 1
        if x not in visitStack:
            dfs(x)

for i in range(1, n+1):
    if findCircuit: break
    dfs(i)
    visitStack = []

print(circuit)
que = deque()
ans = []

def bfs():
    cnt = 0
    while que:
        q = que.popleft()
        for x in link[q]:
            if circuit[x]==0:
                cnt += 1
                que.append(x)
    ans.append(cnt)

for i in range(1, n+1):
    que.append(i)
    bfs()
    que = deque()



print(*ans)