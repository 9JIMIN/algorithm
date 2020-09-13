from collections import deque

n, k = map(int, input().split())
visited = [0]*100001
que = deque([n])
sec = -1

before = [0]*100001
path = []

while que:
    sec += 1
    for _ in range(len(que)):
        x = que.popleft()
        if x == k:
            print(sec)
            while x!=n:
                path.append(x)
                x = before[x]
            path.append(n)

            print(*reversed(path))
            exit()
        nx = [x-1, x+1, 2*x]
        for e in nx:
            if 0<=e<=100000 and visited[e]==0:
                visited[e] = 1
                before[e] = x
                que.append(e)