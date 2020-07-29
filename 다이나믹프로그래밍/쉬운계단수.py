num = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1:
            num[i][j] = 1
        else:
            if 1 <= j <= 8:
                num[i][j] = num[i-1][j-1] + num[i-1][j+1]
            elif j == 0:
                num[i][j] = num[i-1][j+1]
            elif j == 9:
                num[i][j] = num[i-1][j-1]
                
N = int(input())
print(sum(num[N][1:10]) % 1000000000)
