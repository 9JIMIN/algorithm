import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, -1, 1, 2, -2, 1, -1]
for _ in range(int(input())):
    n = int(input())
    chess = [[0]*n for _ in range(n)]
    stax, stay = map(int, input().split())
    endx, endy = map(int, input().split())

    queue = deque()
    queue.append((stax, stay))
    while queue:
        x, y = queue.popleft()
        if x==endx and y==endy: print(chess[x][y]);break
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if chess[nx][ny]==0:
                chess[nx][ny] = chess[x][y]+1
                queue.append((nx, ny))