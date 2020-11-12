import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]     
days = -1   
while queue:
    days += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
for b in box:
    if 0 in b:
        print(-1)
        exit()
print(days)