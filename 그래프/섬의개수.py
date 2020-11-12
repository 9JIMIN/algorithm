

        
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(x, y):
    d[x][y] = '0'
    dx = [-1, 0, 1, 0, -1, 1, -1, 1]
    dy = [0, -1, 0, 1, -1, 1, 1, -1]
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w and d[nx][ny] == '1':
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break
    d = [input().split() for _ in range(h)]

        
    cnt = 0
    for i in range(h):
        for j in range(w):
            if d[i][j] == '1':
                dfs(i, j)
                cnt += 1
    print(cnt)
