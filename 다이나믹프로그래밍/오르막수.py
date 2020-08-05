d = [[1]*10]*1001

for i in range(1, 1001):
    for j in range(1, 10):
        d[i][j] = (d[i-1][j] + d[i][j-1])%10007
print(d[int(input())][-1])