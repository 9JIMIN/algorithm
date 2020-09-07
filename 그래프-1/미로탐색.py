n, m = map(int, input().split())
mp = [[int(i) for i in input()] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

queue = []
queue.append((0, 0))
while queue:
    x, y = queue.pop(0)
    if x==n-1 and y==m-1:
        print(mp[x][y])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny >= m:
            continue
        if mp[nx][ny] == 1:
            mp[nx][ny] = mp[x][y]+1
            queue.append((nx, ny))
