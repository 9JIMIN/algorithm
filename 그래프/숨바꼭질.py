from collections import deque

n, k = map(int, input().split())
visited = [0]*100001
que = deque([n])
sec = -1

while que:
    sec += 1
    for _ in range(len(que)):
        x = que.popleft()
        if x == k:
            print(sec)
            exit()
        nx = [x-1, x+1, 2*x]
        for n in nx:
            if 0<=n<=100000 and visited[n]==0:
                visited[n] = 1
                que.append(n)
