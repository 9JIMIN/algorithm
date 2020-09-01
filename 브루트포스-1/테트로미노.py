n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def find(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                next_x = x+tetromino[i][j][0] # x 좌표
                next_y = y+tetromino[i][j][1] # y 좌표
                result += board[next_x][next_y]
            except IndexError:
                continue
        answer = max(answer, result)
        
def solve():
    for i in range (n):
        for j in range(m):
            find(i, j)
            
answer = 0
solve()
print(answer)