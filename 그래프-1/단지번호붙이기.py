n = int(input())
d = [list(input()) for _ in range(n)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
apt = []

def dfs(x, y):
    global cnt
    d[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if d[nx][ny] == '1':
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if d[i][j] == '1':
            cnt = 0 
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
print(*sorted(apt))
    
