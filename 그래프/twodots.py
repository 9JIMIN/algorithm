import sys
input = sys.stdin.readline

n, m = map(int, input().split())
game = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

flag = False

def dfs(x, y, c):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx<0 or ny<0 or nx>=n or ny>=m: 
            continue
        if game[nx][ny]==game[x][y] and visited[nx][ny]==0:
            visited[nx][ny] = 1
            dfs(nx, ny, c+1)
            visited[nx][ny] = 0
        elif game[nx][ny]==game[x][y] and visited[nx][ny]==2 and c>=3:
            print("Yes")
            exit()
            
for i in range(n):
    for j in range(m):
        visited[i][j] = 2
        dfs(i, j, 0)
        visited[i][j] = 0
print("No")