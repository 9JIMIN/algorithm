# bfs로 탐색하며, 각 노드의 색을 1, 2로 저장한다. 
# 현재노드에 연결된 노드의 색이 같으면, 탐색을 중단하고 NO를 출력.
# 큐가 빌때까지 탐색을 계속한다.
from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    link = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)

    color = [0 for _ in range(v+1)]
    stop = False

    for i in range(1, v+1): 
        if stop: break
        if color[i]: continue

        color[i] = 1
        queue = deque([i])
        
        while queue and not stop:
            q = queue.popleft()
            diffcolor = 3 - color[q]
            for k in link[q]:
                if color[k] == 0:
                    color[k] = diffcolor
                    queue.append(k)
                elif color[k] == color[q]:
                    stop = True
                    break

    print('YES' if not stop else 'NO')
